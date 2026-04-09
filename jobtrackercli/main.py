import typer
from jobtrackercli.ui.banner import show_banner
from jobtrackercli.ui.menu import show_menu
from jobtrackercli.commands import add_job, view_jobs, update_job, delete_job, generate_sankey_graph

app = typer.Typer()

@app.command()
def start():
    show_banner()
    menu()
    
def menu():
    menuChoice = show_menu()
    while True:
        if menuChoice == 'Add Job':
            add_job()
        elif menuChoice == 'View Jobs':
            view_jobs()
        elif menuChoice == 'Update Job':
            update_job()
        elif menuChoice == 'Delete Job':
            delete_job()
        elif menuChoice == 'Generate Sankey Graph':
            generate_sankey_graph()
        elif menuChoice == 'Exit':
            print("Exiting...")
            exit(0)
        else:
            print("Invalid choice.")
        
        menuChoice = show_menu()