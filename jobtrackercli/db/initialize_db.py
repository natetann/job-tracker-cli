import sqlite3
from pathlib import Path

DB_PATH = Path("job_tracker_cli.db")

def initialize_db():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()

    # Create if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL,
            type TEXT NOT NULL,
            status TEXT NOT NULL,
            date_added TEXT NOT NULL
        )
    ''')
    connection.commit()