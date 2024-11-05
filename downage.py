from datetime import datetime
import uuid
from downtime_db_conn import DowntimeDatabase

class Downage:
    def __init__(self, name, location, eqname, eqid, details, id = None, timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), emails_sent = False,resolved=False, time_resolved=None, time_to_resolve=None):
        self.id = id if id is not None else str(uuid.uuid4())
        self.name = name
        self.location = location
        self.eqname = eqname
        self.eqid = eqid
        self.details = details
        self.resolved = resolved
        self.emails_sent = emails_sent
        self.time_resolved = time_resolved
        self.time_to_resolve = time_to_resolve

        if isinstance(timestamp, str):
            self.timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        elif isinstance(timestamp, datetime):
            self.timestamp = timestamp
        else:
            self.timestamp = None

        self.email_handler()

    def __repr__(self):
        # Customize how the object is displayed when printed
        return (f"Downage(id={self.id!r}, name={self.name!r}, location={self.location!r}, "
                f"eqname={self.eqname!r}, eqid={self.eqid!r}, details={self.details!r}, "
                f"timestamp={self.timestamp!r}, resolved={self.resolved!r}, "
                f"emails_sent={self.emails_sent!r}, time_resolved={self.time_resolved!r}, "
                f"time_to_resolve={self.time_to_resolve!r})")
    
    def elapsed_time(self):
        elapsed_time = datetime.now() - self.timestamp
        elapsed_secs = int(elapsed_time.total_seconds())
        return elapsed_secs

    def elapsed_time_string(self):
        total_seconds = self.elapsed_time()
        days, hremainder = divmod(total_seconds, 86400)
        hours, mremainder = divmod(hremainder, 3600)
        minutes, seconds = divmod(mremainder, 60)

        # Format the output
        if hours > 0:
            if hours >= 24:
                result = f"{days}d {hours}h ago"
            else:
                result = f"{hours}h {minutes}m ago"
        else:
            result = f"{minutes}m ago"

        return result

    def email_handler(self):
        if self.emails_sent == False:
            #call email_sender

            db_instance = DowntimeDatabase()
            db_instance.update_emails_sent(self.id)


# # Example usage
# # Create a Downage object when users submit a downtime
# new_downage = Downage(name="SSPA Line", location="Production Line 1", details="Machine failure")
# print(new_downage)
