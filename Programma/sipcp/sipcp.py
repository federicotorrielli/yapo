#!/usr/bin/env python

import time

import typer
import yaml
import xml.etree.ElementTree as ET
import configparser
from fuzzywuzzy import fuzz
from SPARQLWrapper import SPARQLWrapper, SPARQLExceptions, GET, DIGEST, JSON, POST, XML
from urllib import error

app = typer.Typer()
dburl = "http://192.168.1.57:7200/repositories/yapo"


def query1(company: str):
    """
    Given a company it returns all the products that
    are currently sold by that company
    :param company:
    :return: products
    """
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX owl: <http://www.w3.org/2002/07/owl#>\
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\
            PREFIX yapo: <https://evilscript.altervista.org/yapo.owl#>\
            SELECT ?prod WHERE{\
                ?prod rdf:type yapo:Product.\
                ?company rdf:type yapo:Company;\
                yapo:sells ?prod.\
            FILTER(?company = yapo:" + company + ")\
            }"


def query2(company: str):
    """
    Given a company it returns all the subcompanies related
    to the input company
    :param company:
    :return: companies
    """
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX owl: <http://www.w3.org/2002/07/owl#>\
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\
            PREFIX yapo: <https://evilscript.altervista.org/yapo.owl#>\
            SELECT ?companyTo WHERE{\
                ?companyTo rdf:type yapo:Company.\
                ?company rdf:type yapo:Company;\
                yapo:manufacturesTo ?companyTo.\
                FILTER(?company = yapo:" + company + ")\
            }"


def query3(product: str):
    """
    Given a product, it returns the products that have the same
    CPU type of the given products
    :param product:
    """
    return "PREFIX wd: <http://www.wikidata.org/entity/>\
            PREFIX wdt: <http://www.wikidata.org/prop/direct/>\
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
            PREFIX yapo: <https://evilscript.altervista.org/yapo.owl#>\
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            SELECT ?prodLabel WHERE {\
            ?device rdf:type yapo:Device;\
                yapo:CpuType ?cpu.\
            SERVICE <https://query.wikidata.org/sparql> {\
                ?chip wdt:P31 wd:Q610398;\
                    rdfs:label ?label;\
                    wdt:P1535 ?prod.\
                ?prod rdfs:label ?prodLabel.\
            FILTER (?device = yapo:" + product + " && lang(?prodLabel) = 'it' && lang(?label) = 'it' && regex(?label, ?cpu)).\
            }\
            }"


def query4(person: str):
    """
    Given a user, it returns all the products that the
    user bought from one of the companies listed in the
    yapo itself
    :param person:
    :return: products
    """
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX yapo: <https://evilscript.altervista.org/yapo.owl#>\
            SELECT ?prod WHERE{\
                ?user rdf:type yapo:User;\
                yapo:buysProduct ?prod.\
                FILTER (?user = yapo:" + person + ")\
            }"


def query5(price: str):
    """
    Given a price, it returns all the smartphones that cost
    more than that price, ordered from the least expensive
    to the most
    :param price:
    :return: products
    """
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX owl: <http://www.w3.org/2002/07/owl#>\
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\
            PREFIX yapo: <https://evilscript.altervista.org/yapo.owl#>\
            PREFIX price: <http://www.ontologydesignpatterns.org/cp/owl/price.owl#>\
            SELECT ?prod ?brand ?price WHERE {\
                ?brand rdf:type yapo:Company.\
                ?price rdf:type price:Price;\
                    price:hasValue ?v.\
                ?prod rdf:type yapo:Smartphone;\
                    yapo:hasBrand ?brand;\
                    price:hasPrice ?price.\
                FILTER (?v >= '" + price + "'^^xsd:float)\
            }\
            ORDER BY ?price"


def query6():
    """
    Returns all the known smartphones
    and compatible smartwatches with them
    """
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX yapo: <https://evilscript.altervista.org/yapo.owl#>\
            PREFIX price: <http://www.ontologydesignpatterns.org/cp/owl/price.owl#>\
            SELECT ?smartwatch ?brand ?pricesmartwatch ?smartphone WHERE { \
                ?brand rdf:type yapo:Company.\
                ?pricesmartwatch rdf:type price:Price.\
                ?smartphone rdf:type yapo:Smartphone.\
                ?smartwatch rdf:type yapo:Smartwatch;\
                    yapo:compatibleWith ?smartphone;\
                    yapo:hasBrand ?brand;\
                    price:hasPrice ?pricesmartwatch.\
            }"


def query7(smartphone: str):
    """
    Returns the list of cables compatible with that
    smartphone
    """
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX yapo: <https://evilscript.altervista.org/yapo.owl#>\
            SELECT ?smartp ?cable WHERE {\
                ?cable rdf:type yapo:Cable.\
                ?smartp rdf:type yapo:Smartphone;\
                    yapo:containsInBox ?cable.\
                FILTER(?smartp = yapo:" + smartphone + ")\
            }"


def query8(device: str):
    """
    Returns the instagram profile of the company producing
    the input device
    :param device:
    :return: the instagram profile of the maker of the device
    """
    return "PREFIX wd: <http://www.wikidata.org/entity/>\
            PREFIX wdt: <http://www.wikidata.org/prop/direct/>\
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
            PREFIX yapo: <https://evilscript.altervista.org/yapo.owl#>\
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            SELECT ?company ?labelCompany ?labelbrand ?usernameIG WHERE {\
                ?device rdf:type yapo:Device;\
                        yapo:hasBrand ?brand.\
                ?brand rdf:type yapo:Company;\
                       rdfs:label ?labelbrand.\
                SERVICE <https://query.wikidata.org/sparql> {\
                    ?company wdt:P31 wd:Q4830453;\
                        wdt:P2003 ?usernameIG;\
                        rdfs:label ?labelCompany.\
                    FILTER (?device = yapo:" + device + " && lang(?labelCompany) = " \
                                                        "'it' && STR(?labelCompany) = STR(?labelbrand)).\
                }\
            }"


def query9(company, brand):
    """
    Searches for all the product sold by :brand
    on the :company site and returns if it's sold there
    :param company:
    :param brand:
    """
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX yapo: <https://evilscript.altervista.org/yapo.owl#>\
            ASK {\
                ?company yapo:sells ?earPlugs.\
                ?earPlugs rdf:type yapo:EarPlugs.\
                ?company rdf:type yapo:Company.\
                ?brand rdf:type yapo:Company;\
                    yapo:isBrandOf ?earPlugs.\
                FILTER(?company = yapo:" + company + " && ?brand = yapo:" + brand + ").\
            }"


def query10(price: str):
    """
    Given a price, it returns all the smartphones that cost
    more than that price, ordered from the least expensive
    to the most, matched with compatible smartwatch
    :param price:
    :return: products
    """
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\
            PREFIX yapo: <https://evilscript.altervista.org/yapo.owl#>\
            PREFIX price: <http://www.ontologydesignpatterns.org/cp/owl/price.owl#>\
            SELECT ?smartw ?brand ?pricesmartw ?smartp ?pricesmartp WHERE {\
            ?brand rdf:type yapo:Company.\
            ?pricesmartw rdf:type price:Price.\
            ?pricesmartp rdf:type price:Price;\
                price:hasValue ?vsmartp.\
            ?smartp rdf:type yapo:Smartphone;\
                price:hasPrice ?pricesmartp.\
            ?smartw rdf:type yapo:Smartwatch;\
                yapo:compatibleWith ?smartp;\
                yapo:hasBrand ?brand;\
                price:hasPrice ?pricesmartw.\
            FILTER (?vsmartp >= \"" + price + "\"^^xsd:float)\
            }"


def fuzz_check(colonna, to_check):
    """
    Checks the most similar element from column
    to column
    :param colonna:
    :param to_check:
    :return: a list of unique column elements
    """
    newcolonna = set()
    for elem in colonna:
        for elem2 in to_check:
            if fuzz.ratio(elem.lower(), elem2.lower()) > 85:
                newcolonna.add(elem)
    return list(newcolonna)


def show_results(results: dict, opt_column: str):
    columns = []
    # First, we take the colums that the user wants to see from input or from the optional parameter
    print("Le colonne disponibili dalla query sono: ", end="")
    for key, value in results["results"].items():
        if len(value) > 0:
            for kex in value[0].keys():
                columns.append(kex)
                print(kex, end=" ")
    print("")
    if opt_column == "":
        colonna = input("Inserisci il nome della colonne che vuoi visualizzare, separate da una virgola: ").split(",")
        colonna = fuzz_check(columns, colonna)
    else:
        colonna = opt_column.split(",")

    # We initialize a cool progressbar that will be showed during slow online queries
    with typer.progressbar(results["results"]["bindings"], label="Progress") as progress:
        if len(results["results"]["bindings"]) == 0:
            typer.secho("Nessun dato disponibile, prova a modificare la query!", fg=typer.colors.RED)
        else:
            for result in progress:
                for res in colonna:
                    try:
                        print(f"{result[res]['value']}", end=" || ")
                    except KeyError as kerr:
                        typer.secho(f"La colonna {kerr.args[0]} non esiste!", fg=typer.colors.RED, err=True)
                print("")
                time.sleep(0.001)

            confirm = typer.confirm("Vuoi esportare i tuoi dati in un file?")
            if confirm:
                # If the user says so, we can output the results (even the columns that weren't shown)
                file_name = input("Inserisci il nome del file: ")
                with open(file_name, "w") as text_file:
                    pretty_output = yaml.dump(results, default_flow_style=False)
                    print(pretty_output, file=text_file)
                typer.secho(f"File {file_name} correttamente creato!", fg=typer.colors.BRIGHT_GREEN)


def do_query(sqlery: str, opt_column: str = "", update=False, ask=False):
    # First we connect to the Database, the link is different from machine to machine
    # You can find it under Setup/Repositories and then yapo --> chain icon
    config = configparser.ConfigParser()
    global dburl
    if len(config.read("config.ini")) == 0:
        # We check if it's the first time that the user ran the program
        # if it is, we create a new config file with the server url and
        # we stop the current query
        confirmation = typer.confirm(f"Sembra essere la prima volta che utilizzi il programma..."
                                     f" Il server pre-impostato è {dburl}, vuoi cambiarlo?")
        if confirmation:
            change_server()
        else:
            change_server(dburl)
        return

    # If the config already exists, we take the url from there
    dburl = config["GraphDB"]["url"]

    sparql = SPARQLWrapper(dburl)

    sparql.setHTTPAuth(DIGEST)
    sparql.setCredentials("database", "test")
    if ask:
        sparql.setMethod(GET)
        sparql.setReturnFormat(XML)
    elif not update:
        sparql.setMethod(GET)
        sparql.setReturnFormat(JSON)
    else:
        sparql.setMethod(POST)
    sparql.setQuery(sqlery)
    # Then we recover the query results with a try except
    try:
        # Results are stored in JSON
        if not update:
            ret = sparql.queryAndConvert()
            if not ask:
                show_results(ret, opt_column)
            else:
                return ret.toxml()
        else:
            sparql.query()
            typer.secho("Operazione effettuata!", fg=typer.colors.GREEN)
    except SPARQLExceptions.EndPointNotFound as err:
        typer.secho(f"Errore: non riesco a trovare il server GraphDB!", err=True, fg=typer.colors.RED)
        typer.echo(err, err=True)
    except error.URLError as err:
        typer.secho("Errore: il server GraphDB sembra spento o non correttamente avviato, accertati del suo "
                    "funzionamento!", err=True, fg=typer.colors.RED)
        confirm = typer.confirm("Vuoi avere altre informazioni sull'errore?")
        if confirm:
            typer.echo(err, err=True)
    except SPARQLExceptions.QueryBadFormed as err:
        typer.secho("La query in input non è corretta, accertati che sia scritta correttamente e non contenga"
                    " doppi apici nel caso in cui tu sia in standard query mode!", err=True, fg=typer.colors.RED)
        confirm = typer.confirm("Vuoi avere altre informazioni sull'errore?")
        if confirm:
            typer.echo(err, err=True)
    # Then, we show the results, or the error if it enters in the except


@app.command()
def query(query_text: str):
    """
    Queries the text query on yapo.

    Only SELECT queries are accepted
    """
    query_styled = typer.style(query_text, fg=typer.colors.BRIGHT_GREEN, bold=True)
    typer.echo(f"La tua query: {query_styled}")

    # Processing the query and showing the progress bar
    do_query(query_text)


@app.command()
def query_smartphone(base_price: str):
    """
    Given a price, it returns all the smartphones that cost
    more than that price, ordered from the least expensive
    to the most
    """
    do_query(query5(base_price), "prod,brand,price")


@app.command()
def query_smartwatch_smartphone(base_price: str):
    """
    Given a price, it returns all the smartphones that cost
    more than that price, ordered from the least expensive
    to the most, matched with compatible smartwatch
    """
    do_query(query10(base_price), "smartw,brand,pricesmartw,smartp,pricesmartp")


@app.command()
def query_product(company: str):
    """
    Queries all the products sold by the
    input company
    """
    do_query(query1(company), "prod")


@app.command()
def query_subcompanies(company: str):
    """
    Queries all the companies that work
    for the input company
    """
    do_query(query2(company), "companyTo")


@app.command()
def query_from_text():
    """
    Takes a query from a file called do.txt
    Every query must be separated with these characters ||

    Only SELECT queries are accepted
    """
    with open("do.txt", "r") as file:
        text = file.read().split("||")
        num = 1
        for t in text:
            typer.secho(f"Risultato della query numero {num}: ", fg=typer.colors.BRIGHT_BLUE)
            do_query(t)
            num = num + 1


@app.command()
def compatible_smartphones():
    """
    Returns all the compatibility options for smartwatches
    and smartphones
    """
    do_query(query6(), "smartwatch,smartphone")


@app.command()
def compatible_cables(smartphone: str):
    """
    Returns the list of cables compatible with that
    smartphone
    """
    do_query(query7(smartphone), "cable")


@app.command()
def myproducts(user: str):
    """
    Takes the user and returns all the products
    that the user bought from yapo
    """
    do_query(query4(user), "prod")


@app.command()
def search_from_cpu(product: str):
    """
    Takes the product name and returns the
    products that have the same CPU from WikiData
    """
    do_query(query3(product), "prodLabel")


@app.command()
def search_ig_profile(device: str):
    """
    Returns the instagram profile of the company producing
    the input device
    """
    do_query(query8(device), "usernameIG")


@app.command()
def search_brand(company: str, brand: str):
    """
    Searches for all the product sold by :brand
    on the :company site and returns if it's sold there
    """
    responseb = do_query(query9(company, brand), ask=True)
    response_xml = ET.XML(responseb)
    if response_xml[1].text == 'true':
        typer.secho(f"Il brand {brand} è venduto sul sito {company}!", fg=typer.colors.GREEN)
    else:
        typer.secho(f"Il brand {brand} NON è venduto sul sito {company}!", fg=typer.colors.RED)


@app.command()
def change_server(opt_url=""):
    """
    Changes the server URL pointing to the GraphDB endpoint
    and saves it in a file called config.ini
    :return:
    """
    # Create the config.ini object and ask which server to put in
    config_obj = configparser.ConfigParser()
    if opt_url == "":
        newurl = input("Inserire l'URL nuovo: ")
    else:
        newurl = opt_url
    config_obj["GraphDB"] = {
        "url": newurl
    }
    with open("config.ini", "w") as conf:
        config_obj.write(conf)


if __name__ == '__main__':
    app()
