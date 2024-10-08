import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from downtime_display import DowntimeDisplay

class DowntimeEntry:
    def __init__(self, db):
        self.db = db
        self.root = ttk.Window(themename="solar")  # Choose a theme, e.g., "solar"
        self.root.title("Downtime Entry")

        # Create the input form using ttkbootstrap
        self.label = ttk.Label(self.root, text="Enter Downtime Information:", bootstyle="primary")
        self.label.pack(padx=10, pady=10)

        self.location_label = ttk.Label(self.root, text="Location:", bootstyle="info")
        self.location_label.pack(padx=10, pady=5)

        self.location_entry = ttk.Entry(self.root)
        self.location_entry.pack(padx=10, pady=5)

        self.submit_button = ttk.Button(self.root, text="Submit", bootstyle="success", command=self.submit)
        self.submit_button.pack(padx=10, pady=10)

         # Button to open the display window
        self.display_button = ttk.Button(self.root, text="Open Display Window", bootstyle="info", command=self.open_display)
        self.display_button.pack(padx=10, pady=10)

    def submit(self):
        location = self.location_entry.get()
        self.db.add_downtime(location)
        print("Downtime added successfully!")
        
    def open_display(self):
        # Open the downtime display window when the button is clicked
        downtime_display_window = DowntimeDisplay(self.db)
        downtime_display_window.start()

    def start(self):
        self.root.mainloop()
