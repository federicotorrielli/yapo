import typer
import sparql
import time

app = typer.Typer()
# TODO: import query from a text file


def do_query(sqlery: str):
    # First we connect to the Database
    server = sparql.Service("localhost:7200", "utf-8", "GET")
    # Then we ask for the result and we show the progress bar
    progress_bar()
    result = server.query(sqlery)


def progress_bar():
    total = 0
    with typer.progressbar(range(100)) as progress:
        for value in progress:
            time.sleep(0.01)
            total += 1
    typer.echo(f"Processed {total} things.")


@app.command()
def welcome(name: str):
    typer.echo(f"Welcome, {name}! Type your SPARQL query with the query command.")


@app.command()
def query(query_text: str):
    query_styled = typer.style(query_text, fg=typer.colors.BRIGHT_GREEN, bold=True)
    typer.echo(f"Your query was {query_styled}\nI will now start to process it!")

    # Processing the query and showing the progress bar
    do_query(query_text)


if __name__ == '__main__':
    app()
