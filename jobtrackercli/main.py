import typer
from jobtrackercli.ui.banner import show_banner
from jobtrackercli.ui.menu import show_menu

app = typer.Typer()

@app.command()
def start():
    show_banner()
    show_menu()