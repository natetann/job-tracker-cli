import rich
import sqlite3
from jobtrackercli.db.initialize_db import DB_PATH

def view_jobs():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT id, title, company, location, type, status, date_added FROM jobs')
        # Return as a list of tuples
        jobs = cursor.fetchall()

    # If list is empty
    if not jobs:
        print("No jobs found.")
        return
    
    # Build table
    table = rich.table.Table()
    table.add_column("ID", justify="center", style="grey42")
    table.add_column("Title", justify="center", style="grey93")
    table.add_column("Company", justify="center", style="cyan")
    table.add_column("Location", justify="center", style="grey82")
    table.add_column("Type", justify="center", style="dark_cyan")
    table.add_column("Status", justify="center", style="green")
    table.add_column("Date Added", justify="center", style="grey42")
    for job in jobs:
        table.add_row(str(job[0]), job[1], job[2], job[3], job[4], job[5], job[6])
    rich.print(table)