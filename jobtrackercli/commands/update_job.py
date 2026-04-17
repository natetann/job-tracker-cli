import sqlite3
import jobtrackercli.db.initialize_db as db

def update_job(id: str, field: str, value: str):
    with sqlite3.connect(db.DB_PATH) as connection:
        cursor = connection.cursor()
        # Fetch old value for success message
        queryOld = f'SELECT {field} FROM jobs WHERE id = ?'
        cursor.execute(queryOld, (id,))
        row = cursor.fetchone()
        oldValue = row[0]

        # Update with new value
        query = f'UPDATE jobs SET {field} = ? WHERE id = ?'
        cursor.execute(query, (value, id))
        connection.commit()
    return oldValue