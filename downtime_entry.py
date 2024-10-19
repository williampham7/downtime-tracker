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
        self.main_corner_y = (self.screen_height // 2) - (self.main_window_y // 2) - self.screen_height // 15
        self.main_geometry = (f"{self.main_window_x}x{self.main_window_y}+{self.main_corner_x}+{self.main_corner_y}")
        self.root.geometry(self.main_geometry)

        # Make sure that the main frame fills the entire window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Main frame to divide left and right sections, expand to fit entire window
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Configure columns and rows in main_frame
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)  # For spacing between entry and active downages
        self.main_frame.grid_columnconfigure(3, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Left frame for entering new downtime
        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.grid(row=0, column=0, padx=20, pady=10, sticky=N)

        # Title for the left frame
        self.entry_label = ttk.Label(self.left_frame, text="Enter New Downage", bootstyle="primary")
        self.entry_label.grid(row=0, column=0, pady=10)

        # Name input
        self.name_label = ttk.Label(self.left_frame, text="Name:")
        self.name_label.grid(row=1, column=0, sticky=W)
        self.name_entry = ttk.Entry(self.left_frame, width=30)
        self.name_entry.grid(row=2, column=0, pady=5)

        # Production line / area input
        self.line_label = ttk.Label(self.left_frame, text="Prod. Line / Area:")
        self.line_label.grid(row=3, column=0, sticky=W)
        self.line_entry = ttk.Entry(self.left_frame, width=30)
        self.line_entry.grid(row=4, column=0, pady=5)

        # Details input
        self.details_label = ttk.Label(self.left_frame, text="Details:")
        self.details_label.grid(row=5, column=0, sticky=W)
        self.details_entry = ttk.Entry(self.left_frame, width=30)
        self.details_entry.grid(row=6, column=0, pady=5)

        # Submit button
        self.submit_button = ttk.Button(self.left_frame, text="Submit", bootstyle="success", command=self.submit)
        self.submit_button.grid(row=7, column=0, pady=10)

        # Divider between left and right
        self.divider = ttk.Separator(self.main_frame, orient=VERTICAL)
        self.divider.grid(row=0, column=1, padx=20, pady=10, sticky="ns")

        # Right frame for active downtimes, expanding to take up available space
        self.right_frame = ttk.Frame(self.main_frame)
        self.right_frame.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")

        # Title for the right frame
        self.active_label = ttk.Label(self.right_frame, text="Active Downages", bootstyle="primary")
        self.active_label.grid(row=0, column=0, pady=10)

        # Example of active downtime event (this would be dynamic in real usage)
        self.create_active_downtime(self.right_frame, "SSPA Line", "3h 25m ago", "danger", 0)
        self.create_active_downtime(self.right_frame, "Chip & Wire", "1h 15m ago", "warning", 1)

        # Button to open the display window, moving it to its own row to avoid overlap
        self.display_button = ttk.Button(self.main_frame, text="Open Viewer", bootstyle="info", command=self.open_viewer)
        self.display_button.grid(row=0, column=2, padx=20, pady=10, sticky="ne")

    def create_active_downtime(self, parent, line_name, time_elapsed, icon_color, row):
        """Helper function to create an active downtime widget."""
        # Create frame for downtime
        active_downtime = ttk.Frame(parent, bootstyle="secondary")
        active_downtime.grid(row=row + 1, column=0, pady=10, sticky=W + E)

        # Circular icon
        self.icon_label = ttk.Label(active_downtime, text="●", bootstyle=icon_color)
        self.icon_label.grid(row=0, column=0, padx=10, pady=5)
 
        # Downtime details (line and time elapsed)
        downtime_label = ttk.Label(active_downtime, text=f"{line_name}\n{time_elapsed}", bootstyle="default")
        downtime_label.grid(row=0, column=1, padx=10, pady=5)

        # Resolve and alert buttons
        resolve_button = ttk.Button(active_downtime, text="Resolve", bootstyle="danger-outline")
        resolve_button.grid(row=0, column=2, padx=5)

        alert_button = ttk.Button(active_downtime, text="Alert", bootstyle="warning-outline")
        alert_button.grid(row=0, column=3, padx=5)

    def submit(self):
        name = self.name_entry.get()
        location = self.line_entry.get()
        details = self.details_entry.get()

        # Create a new Downage object
        new_downage = Downage(name, location, details)

        # Add to database or perform other logic
        self.db.add_downtime(new_downage)

        print(f"New downtime submitted: {new_downage}")

    def open_viewer(self):
        downtime_display_window = DowntimeDisplay(self.db)
        downtime_display_window.start()

    def start(self):
        self.root.mainloop()
