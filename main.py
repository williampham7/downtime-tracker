from downtime_entry import DowntimeEntry
from downtime_db import DowntimeDatabase

def main():
    db = DowntimeDatabase()  # Initialize the database connection
    downtime_entry_window = DowntimeEntry(db)  # Open only the entry window at startup
    downtime_entry_window.start()

if __name__ == "__main__":
    main()