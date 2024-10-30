from datetime import datetime
import uuid

class Downage:
    def __init__(self, name, location, eqname, eqid, details):
        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location
        self.eqname = eqname
        self.eqid = eqid
        self.details = details
        self.timestamp = datetime.now() 
        self.resolved = False
        self.stage = 0

        # self.send_initial_message()

    def __repr__(self):
        # Customize how the object is displayed when printed
        return (f"Downage(name='{self.name}', location='{self.location}', eqname='{self.eqname}', eqid='{self.eqid}', "
                f"details='{self.details}', resolved='{self.resolved}', 'timestamp='{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}')")
    
    def elapsed_time(self):

        time_difference = datetime.now() - self.timestamp
        total_seconds = int(time_difference.total_seconds())
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

    def increment_stage(self):
        self.stage += 1
        self.action(self)

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
