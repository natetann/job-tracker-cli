import typer
from jobtrackercli.ui import utils
from jobtrackercli.db.initialize_db import initialize_db
from jobtrackercli.commands import (
    add_job,
    view_jobs,
    update_job,
    delete_job,
    generate_sankey_graph,
)

app = typer.Typer()

def start():
    utils.show_banner()
    initialize_db()
    menu()
    
def menu():
    menuChoice = utils.show_menu()
    while True:
        if menuChoice == 'Add Job':
            title, company, location, type, status = utils.prompt_job_details()
            add_job(title, company, location, type, status)
            utils.show_text(f"{company} application added successfully!", "success")
        elif menuChoice == 'View Jobs':
            view_jobs()
        elif menuChoice == 'Update Job':
            update_job()
        elif menuChoice == 'Delete Job':
            delete_job()
        elif menuChoice == 'Generate Sankey Graph':
            generate_sankey_graph()
        elif menuChoice == 'Exit':
            utils.show_text("Goodbye!", "info")
            exit()
        else:
            utils.show_text("Invalid choice.", "error")

        menuChoice = utils.show_menu()