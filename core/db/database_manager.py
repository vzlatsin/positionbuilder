import sqlite3

class DatabaseManager:
    def __init__(self, db_path="positionbuilder.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def execute_script(self, script_path):
        with self.connect() as conn:
            with open(script_path, "r") as f:
                conn.executescript(f.read())
            conn.commit()

    def execute_query(self, query, params=None):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            conn.commit()
            return cursor

    def fetch_all(self, query, params=None):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchall()
