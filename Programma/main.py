import time
import typer
import yaml
from SPARQLWrapper import SPARQLWrapper, SPARQLExceptions, GET, DIGEST, JSON

app = typer.Typer()


# TODO: Take all the products from the productCatalog
# TODO: Take all the required data from the productCatalog
# TODO: Query other data platforms

def show_results(results):
    colonna = input("Inserisci il nome della colonne che vuoi visualizzare, separate da una virgola: ").split(",")

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
        file_name = input("Inserisci il nome del file: ")
        with open(file_name, "w") as text_file:
            pretty_output = yaml.dump(results, default_flow_style=False)
            print(pretty_output, file=text_file)
        typer.secho(f"File {file_name} correttamente creato!", fg=typer.colors.BRIGHT_GREEN)


def do_query(sqlery: str):
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
        # Results are stored in JSON ff
        show_results(ret)
    except SPARQLExceptions.EndPointNotFound as err:
        typer.secho(f"Errore: non riesco a trovare il server GraphDB!", fg=typer.colors.RED)
        typer.echo(err)
    # Then, we show the results


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
def query_from_text():
    """
    Takes a query from a file called do.txt
    Every query must be a one-liner only: one query per line.

    Only SELECT queries are accepted
    """
    num_lines = sum(1 for _ in open("do.txt"))
    with open("do.txt", "r") as file:
        for lines in range(num_lines):
            do_query(file.readline())


if __name__ == '__main__':
    app()
