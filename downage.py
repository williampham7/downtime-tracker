from datetime import datetime

class Downage:
    def __init__(self, name, eqname, eqid, location, details):
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
