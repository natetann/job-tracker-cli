import rich
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
    choice = utils.show_menu()
    while True:
        if choice == 'Add Job':
            title, company, location, type, status = utils.prompt_job_details()
            add_job(title, company, location, type, status)
            utils.show_text(f"{company} application added successfully!", "success")

        elif choice == 'View Jobs':
            view_jobs()

        elif choice == 'Update Job':
            view_jobs()
            id, field, value = utils.prompt_update_details()
            if id and field and value:
                oldValue = update_job(id, field, value)
                utils.show_text(f"Job ID {id}'s {field} updated from \"{oldValue}\" -> \"{value}\" successfully!", "success")

        elif choice == 'Delete Job':
            view_jobs()
            id = utils.prompt_delete_id()
            if id:
                delete_job(id)
                utils.show_text(f"Job ID {id} deleted successfully!", "success")

        elif choice == 'Exit':
            utils.show_text("Goodbye!", "info")
            exit()

        else:
            utils.show_text("Invalid choice.", "error")

        choice = utils.show_menu()