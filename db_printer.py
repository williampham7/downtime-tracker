from downtime_db_conn import DowntimeDatabase

def main():
    # Create an instance of the database
    db_instance = DowntimeDatabase()

    # Get all downtime entries
    all_downtimes = db_instance.get_all_downtime()

    # Print each downtime entry
    for entry in all_downtimes:
        print(entry)

if __name__ == "__main__":
    main()