import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime

class DowntimeDisplay:
    def __init__(self, db):
        self.db = db
        self.root = ttk.Window()  # Using a theme for modern look
        self.root.title("Downtime Display")

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.main_window_x = 500
        self.main_window_y = 500
        self.main_corner_x = (self.screen_width // 2) - (self.main_window_x // 2)
        self.main_corner_y = (self.screen_height // 2) - (self.main_window_y // 2) - self.screen_height//15
        self.main_geometry = (f"{self.main_window_x}x{self.main_window_y}+{self.main_corner_x}+{self.main_corner_y}")
        self.root.geometry(self.main_geometry)

        # Title Label
        self.title_label = ttk.Label(self.root, text="Active Downages", bootstyle="primary")
        self.title_label.pack(padx=10, pady=10)

        # Frame to hold the downtimes
        self.downtime_frame = ttk.Frame(self.root)
        self.downtime_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Start the periodic update
        self.update_downtime()

    def format_downage(self, downage):
        # Format the downtime data for display
        name, location, details, timestamp, resolved, stage = downage
        resolved_text = "Resolved" if resolved == 1 else "Unresolved"
        resolved_color = "success" if resolved == 1 else "danger"
        
        try:
            # Convert timestamp to datetime object, including microseconds
            timestamp_str = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError as e:
            timestamp_str = "Invalid timestamp"  # Fallback for invalid timestamps

        downtime_string = (f"Name: {name}\n"
                        f"Location: {location}\n"
                        f"Details: {details}\n"
                        f"Time: {timestamp_str.strftime('%Y-%m-%d %H:%M:%S') if isinstance(timestamp_str, datetime) else timestamp_str}\n"
                        f"Stage: {stage}\n"
                        f"Status: {resolved_text}")
        
        return downtime_string, resolved_color

    def update_downtime(self):
        # Clear the frame and refill it with updated downages
        for widget in self.downtime_frame.winfo_children():
            widget.destroy()

        downtimes = self.db.get_all_downtime()
        if not downtimes:
            # Display message if no downtime entries are found
            no_data_label = ttk.Label(self.downtime_frame, text="No active downages.", bootstyle="warning")
            no_data_label.pack(fill="x", padx=10, pady=5)

        for downtime in downtimes:
            downtime_string, resolved_color = self.format_downage(downtime)

            # Frame for each downtime entry
            downtime_item = ttk.Frame(self.downtime_frame, bootstyle="info")
            downtime_item.pack(fill="x", padx=10, pady=5)

            # Downtime information
            downtime_label = ttk.Label(downtime_item, text=downtime_string, anchor="w", justify="left")
            downtime_label.pack(side="left", padx=10, pady=5)

            # Resolved status with color
            #resolve_status = ttk.Label(downtime_item, text="Resolved" if downtime[5] else "Unresolved", bootstyle=resolved_color)
            # resolve_status.pack(side="right", padx=10)

        # Schedule the next update after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_downtime)

    def start(self):
        self.root.mainloop()
