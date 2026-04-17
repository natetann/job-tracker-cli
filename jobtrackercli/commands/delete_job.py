import sqlite3
import jobtrackercli.db.initialize_db as db

def delete_job(id: int):
    with sqlite3.connect(db.DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM jobs WHERE id = ?', (id,))
        connection.commit()