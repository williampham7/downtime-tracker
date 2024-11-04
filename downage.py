from datetime import datetime
import uuid

class Downage:
    def __init__(self, name, location, eqname, eqid, details, id = None, timestamp = datetime.now(), resolved=False, time_resolved=None, time_to_resolve=None):
        self.id = id if id is not None else str(uuid.uuid4())
        self.name = name
        self.location = location
        self.eqname = eqname
        self.eqid = eqid
        self.details = details
        self.resolved = resolved
        self.time_resolved = time_resolved
        self.time_to_resolve = time_to_resolve

        if isinstance(timestamp, str):
            self.timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
        elif isinstance(timestamp, datetime):
            self.timestamp = timestamp
        else:
            self.timestamp = None

        # self.send_initial_message()

    def __repr__(self):
        # Customize how the object is displayed when printed
        return (f"Downage(id='{self.id}, 'name='{self.name}', location='{self.location}', eqname='{self.eqname}', eqid='{self.eqid}', "
                f"details='{self.details}', 'timestamp='{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}', resolved='{self.resolved}', time_resolved='{self.time_resolved}', time_to_resolve='{self.time_to_resolve}')")
    
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
    
    def send_initial_message():
        # send first emails 
        return

    def action(self):
        if self.resolved == True:
            return
        
        if self.stage == 1:
            # send batch 2 emails
            return
        elif self.stage == 2:
            # send batch 2 emails
            return



# # Example usage
# # Create a Downage object when users submit a downtime
# new_downage = Downage(name="SSPA Line", location="Production Line 1", details="Machine failure")
# print(new_downage)
