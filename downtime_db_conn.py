import sqlite3
from datetime import datetime

class DowntimeDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('downtime.db')
        self.cursor = self.connection.cursor()
        self.create_main_table()
       #self.create_unresolved_table()

    def create_main_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS downtime
                            (id TEXT PRIMARY KEY,  -- UUID as TEXT
                             name TEXT,
                             location TEXT,
                             eqname TEXT,
                             eqid TEXT,
                             details TEXT,
                             timestamp DATETIME,
                             resolved BOOLEAN DEFAULT FALSE,
                             time_resolved DATETIME,  -- Added field for time resolved
                             time_to_resolve INTEGER)  -- Added field for time to resolve
                            ''')
        self.connection.commit()

    def add_downtime(self, downage_obj):
        # Insert the Downage object data into the database
        self.cursor.execute('''INSERT INTO downtime (id, name, location, eqname, eqid, details, timestamp, resolved, time_resolved, time_to_resolve) 
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (downage_obj.id,
                             downage_obj.name,
                             downage_obj.location,
                             downage_obj.eqname,
                             downage_obj.eqid,
                             downage_obj.details,
                             downage_obj.timestamp,  # Store as a string
                             downage_obj.resolved,  # Store boolean as int (0 or 1)
                             downage_obj.time_resolved,  # Nullable, can be None
                             downage_obj.time_to_resolve))  # Nullable, can be None
        self.connection.commit()

    def get_all_downtime(self):
        # Retrieve all downtime entries from the database
        self.cursor.execute("SELECT id, name, location, eqname, eqid, details, timestamp, resolved, time_resolved, time_to_resolve FROM downtime")
        return self.cursor.fetchall()
    
    def get_all_unresolved(self):
        # Retrieve all UNRESOLVED Downage entries from the database
        self.cursor.execute("SELECT id, name, location, eqname, eqid, details, timestamp, time_resolved, time_to_resolve FROM downtime WHERE resolved = 0")        
        return self.cursor.fetchall()
    
    def resolve_downtime(self, downtime_id):
        # Update the downtime's resolved field to 1 (resolved) and set time resolved
        time_resolved = datetime.now()
        self.cursor.execute('''UPDATE downtime 
                               SET resolved = TRUE, 
                                   time_resolved = ?, 
                                   time_to_resolve = ? 
                               WHERE id = ?''', 
                            (time_resolved, 
                             (time_resolved - datetime.now()).total_seconds(),  # Calculate time to resolve as needed
                             downtime_id))
        self.connection.commit()

    def __del__(self):
        # Close the database connection
        self.connection.close()
