import sqlite3

class DowntimeDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('downtime.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS downtime
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             location TEXT,
                             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.connection.commit()

    def add_downtime(self, location):
        self.cursor.execute("INSERT INTO downtime (location) VALUES (?)", (location,))
        self.connection.commit()

    def get_all_downtime(self):
        self.cursor.execute("SELECT location, timestamp FROM downtime")
        return self.cursor.fetchall()

    def __del__(self):
        self.connection.close()
