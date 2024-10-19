import sqlite3
from datetime import datetime

class DowntimeDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('downtime.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS downtime
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT,
                             location TEXT,
                             eqname TEXT,
                             eqid TEXT,
                             details TEXT,
                             timestamp DATETIME,
                             resolved INTEGER DEFAULT 0,
                             stage INTEGER DEFAULT 0)''')  # Added new fields for resolved and stage
        self.connection.commit()

    def add_downtime(self, downage_obj):
        # Insert the Downage object data into the database
        self.cursor.execute('''INSERT INTO downtime (name, location, eqname, eqid, details, timestamp, resolved, stage) 
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                            (downage_obj.name,
                             downage_obj.location,
                             downage_obj.eqname,
                             downage_obj.eqid,
                             downage_obj.details,
                             downage_obj.timestamp,  # Store as a string
                             int(downage_obj.resolved),  # Store boolean as int (0 or 1)
                             downage_obj.stage))
        self.connection.commit()

    def get_all_downtime(self):
        # Retrieve all downtime entries from the database
        self.cursor.execute("SELECT name, location, eqname, eqid, details, timestamp, resolved, stage FROM downtime")
        return self.cursor.fetchall()
    
    def get_all_unresolved(self):
        # Retrieve all UNRESOLVED Downage entries from the database
        self.cursor.execute("SELECT nname, location, eqname, eqid, details, timestamp, resolved, stage FROM downtime WHERE resolved = 0")        
        return self.cursor.fetchall()
    
    def resolve_downtime(self, downtime_id):
        # Update the downtime's resolved field to 1 (resolved)
        self.cursor.execute('''UPDATE downtime 
                               SET resolved = 1 
                               WHERE id = ?''', (downtime_id,))
        self.connection.commit()

    def increment_stage(self, downtime_id):
        # Increment the stage field of the specific downtime by 1
        self.cursor.execute('''UPDATE downtime 
                               SET stage = stage + 1 
                               WHERE id = ?''', (downtime_id,))
        self.connection.commit()

    def __del__(self):
        # Close the database connection
        self.connection.close()


