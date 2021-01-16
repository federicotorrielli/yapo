#!/usr/bin/env python

import time

import typer
import yaml
from SPARQLWrapper import SPARQLWrapper, SPARQLExceptions, GET, DIGEST, JSON
from urllib import error

app = typer.Typer()


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
            PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>\
            SELECT ?prod WHERE{\
                ?prod rdf:type sipg:Product.\
                ?company rdf:type sipg:Company;\
                sipg:sells ?prod.\
            FILTER(?company = sipg:" + company + ")\
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
            PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>\
            SELECT ?companyTo WHERE{\
                ?companyTo rdf:type sipg:Company.\
                ?company rdf:type sipg:Company;\
                sipg:manufacturesTo ?companyTo.\
                FILTER(?company = sipg:" + company + ")\
            }"


def query3(product: str):
    """
    Given a product, it returns the cpu type of that product
    :param product:
    :return: cpu type of that product
    """
    return "PREFIX wd: <http://www.wikidata.org/entity/>\
            PREFIX wdt: <http://www.wikidata.org/prop/direct/>\
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
            PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>\
            SELECT ?prod ?cpu WHERE {\
            ?device sipg:CpuType ?cpu.\
            SERVICE <https://query.wikidata.org/sparql> {\
                ?chip wdt:P31 wd:Q610398;\
                rdfs:label ?label;\
                wdt:P1535 ?prod.\
            FILTER (?device = sipg:" + product + " && lang(?label) = 'it' && regex(?label, ?cpu)).\
            }\
            }"


def query4(person: str):
    """
    Given a user, it returns all the products that the
    user bought from one of the companies listed in the
    productCatalog itself
    :param person:
    :return: products
    """
    return "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\
            PREFIX sipg: <https://evilscript.altervista.org/productCatalog.owl#>\
            SELECT ?prod WHERE{\
                ?user rdf:type sipg:User;\
                sipg:buysProduct ?prod.\
                FILTER (?user = sipg:" + person + ")\
            }"


def show_results(results: dict, opt_column: str):
    # First, we take the colums that the user wants to see from input or from the optional parameter
    print("Le colonne disponibili dalla query sono: ", end="")
    for key, value in results["results"].items():
        for kex in value[0].keys():
            print(kex, end=" ")

    if opt_column == "":
        colonna = input("\nInserisci il nome della colonne che vuoi visualizzare, separate da una virgola: ").split(",")
    else:
        colonna = opt_column.split(",")

    # We initialize a cool progressbar that will be showed during slow online queries
    with typer.progressbar(results["results"]["bindings"], label="Progress") as progress:
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


def do_query(sqlery: str, opt_column: str = ""):
    # First we connect to the Database, the link is different from machine to machine
    # You can find it under Setup/Repositories and then productCatalog --> chain icon
    sparql = SPARQLWrapper("http://192.168.1.57:7200/repositories/productCatalog")
    sparql.setHTTPAuth(DIGEST)
    sparql.setCredentials("database", "test")
    sparql.setMethod(GET)
    # Then we ask for the result and we show the progress bar
    sparql.setQuery(sqlery)
    sparql.setReturnFormat(JSON)
    # Then we recover the query results with a try except
    try:
        ret = sparql.query().convert()
        # Results are stored in JSON
        show_results(ret, opt_column)
    except SPARQLExceptions.EndPointNotFound as err:
        typer.secho(f"Errore: non riesco a trovare il server GraphDB!", fg=typer.colors.RED)
        typer.echo(err)
    except error.URLError:
        typer.secho("Errore: il server GraphDB sembra spento o non correttamente avviato, accertati del suo "
                    "funzionamento!", fg=typer.colors.RED)
    except SPARQLExceptions.QueryBadFormed:
        typer.secho("La query in input non è corretta, accertati che sia scritta correttamente e non contenga"
                    "doppi apici nel caso in cui tu sia in standard query mode!", fg=typer.colors.RED)
    # Then, we show the results, or the error if it enters in the except


@app.command()
def welcome(name: str):
    """
    Shows the welcome message, in italian
    """
    typer.echo(f"Ciao, {name}! Scrivi la tua query SPARQL con il comando query.")


@app.command()
def query(query_text: str):
    """
    Queries the text query on the productCatalog.

    Only SELECT queries are accepted
    """
    query_styled = typer.style(query_text, fg=typer.colors.BRIGHT_GREEN, bold=True)
    typer.echo(f"La tua query: {query_styled}")

    # Processing the query and showing the progress bar
    do_query(query_text)


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
def myproducts(user: str):
    """
    Takes the user and returns all the products
    that the user bought from the productCatalog
    """
    do_query(query4(user), "prod")


@app.command()
def cputype(product: str):
    """
    Takes the product name and returns the
    CPU type of the product from WikiData
    """
    do_query(query3(product), "prod,cpu")


if __name__ == '__main__':
    app()
