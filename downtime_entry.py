import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from downtime_display import DowntimeDisplay
from downage import Downage

class DowntimeEntry:
    def __init__(self, db):
        self.db = db
        self.root = ttk.Window(themename="litera")  # Choose a theme, e.g., "solar"
        self.root.title("Downtime Tracker")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.main_window_x = 800
        self.main_window_y = 500
        self.main_corner_x = (self.screen_width // 2) - (self.main_window_x // 2)
        self.main_corner_y = (self.screen_height // 2) - (self.main_window_y // 2) - self.screen_height//15
        self.main_geometry = (f"{self.main_window_x}x{self.main_window_y}+{self.main_corner_x}+{self.main_corner_y}")
        self.root.geometry(self.main_geometry)

        # Main frame to divide left and right sections
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=TRUE, padx=20, pady=20)

        # Left frame for entering new downtime
        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.grid(row=0, column=0, padx=20, pady=10)

        # Title for the left frame
        self.entry_label = ttk.Label(self.left_frame, text="Enter New Downage", bootstyle="primary")
        self.entry_label.grid(row=0, column=0, pady=10)

        # Name input
        self.name_label = ttk.Label(self.left_frame, text="Name:")
        self.name_label.grid(row=1, column=0, sticky=W)
        self.name_entry = ttk.Entry(self.left_frame, width = 20)
        self.name_entry.grid(row=2, column=0, pady=5)

        # Production line / area input
        self.line_label = ttk.Label(self.left_frame, text="Prod. Line / Area:")
        self.line_label.grid(row=3, column=0, sticky=W)
        self.line_entry = ttk.Entry(self.left_frame, width = 20)
        self.line_entry.grid(row=4, column=0, pady=5)

        # Details input
        self.details_label = ttk.Label(self.left_frame, text="Details:")
        self.details_label.grid(row=5, column=0, sticky=W)
        self.details_entry = ttk.Entry(self.left_frame, width = 20)
        self.details_entry.grid(row=6, column=0, pady=5)

        # Submit button
        self.submit_button = ttk.Button(self.left_frame, text="Submit", bootstyle="success", command=self.submit)
        self.submit_button.grid(row=7, column=0, pady=10)

        # Right frame for active downtimes
        self.right_frame = ttk.Frame(self.main_frame)
        self.right_frame.grid(row=0, column=1, padx=20, pady=10, sticky=N)

        # Title for the right frame
        self.active_label = ttk.Label(self.right_frame, text="Active Downages", bootstyle="primary")
        self.active_label.grid(row=0, column=0, pady=10)

        # Example of active downtime event (this would be dynamic in real usage)
        self.active_downtime = ttk.Frame(self.right_frame, bootstyle="secondary")
        self.active_downtime.grid(row=1, column=0, pady=10, sticky=W+E)
        
        # Display downtime details
        self.downtime_label = ttk.Label(self.active_downtime, text="SSPA Line\n3h 25m ago", bootstyle="danger")
        self.downtime_label.grid(row=0, column=0, padx=10, pady=5)

        # Resolve and alert buttons
        self.resolve_button = ttk.Button(self.active_downtime, text="Resolve", bootstyle="danger-outline")
        self.resolve_button.grid(row=0, column=1, padx=5)

        self.alert_button = ttk.Button(self.active_downtime, text="Alert", bootstyle="warning-outline")
        self.alert_button.grid(row=0, column=2, padx=5)

        # Button to open the display window
        self.display_button = ttk.Button(self.main_frame, text="Open Viewer", bootstyle="info", command=self.open_display)
        self.display_button.grid(row=0, column=1, padx=20, pady=10, sticky="ne")

    def submit(self):
        name = self.name_entry.get()
        location = self.line_entry.get()
        details = self.details_entry.get()

        # Create a new Downage object
        new_downage = Downage(name, location, details)

        # Add to database or perform other logic
        self.db.add_downtime(new_downage)

        print(f"New downtime submitted: {new_downage}")

    def open_display(self):
        downtime_display_window = DowntimeDisplay(self.db)
        downtime_display_window.start()

    def start(self):
        self.root.mainloop()

