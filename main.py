from downtime_entry import DowntimeEntry
from downtime_db_conn import DowntimeDatabase
import ctypes
import os

def main():
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    
    db = DowntimeDatabase()  # Initialize the database connection
    config_path = 'config.json'
    downtime_entry_window = DowntimeEntry(db, config_path)  # Open only the entry window at startup
    downtime_entry_window.start()

if __name__ == "__main__":
    main()