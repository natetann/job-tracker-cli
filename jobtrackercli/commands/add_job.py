import sqlite3
from datetime import date
import jobtrackercli.db.initialize_db as db

def add_job(title: str, company: str, location: str, type: str, status: str, date_added: str = date.today().isoformat()):
    db.initialize_db()
    with sqlite3.connect(db.DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO jobs (title, company, location, type, status, date_added)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, company, location, type, status, date_added))
        connection.commit()
