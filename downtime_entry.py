import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from downtime_viewer import DowntimeViewer
from downage import Downage
from info_window import info_window
from center_window import center_window
import style, json

# SETTINGS
header_font = style.header_font
entry_font = style.entry_font
entry_width = style.entry_width

class DowntimeEntry:
    def __init__(self, db, config_path):
        self.db_instance = db
        self.config_path = config_path
        self.root = ttk.Window()
        self.root.title("Downtime Tracker")
        main_window_x =1100
        main_window_y = 620

        center_window(self.root, main_window_x, main_window_y)

        #config file
        try:
            with open(self.config_path, 'r') as file:
                config_data = json.load(file)
            
            self.line_options = config_data['line_options']
            self.line_options.sort()
        except:
            self.line_options = []

        #VARIABLES 
        #to update the actives panel
        self.dt_list = []
        self.dt_ids = []
        self.id_checklist = []
        # for loop to update time delta between downage upload to current time
        self.update_counter = 0

        self.update_actives

        # styling
        self.style = ttk.Style(theme=style.theme)
        style.set_custom_styles(self)

        # Make sure that the main frame fills the entire window
        self.root.grid_columnconfigure(0, weight=1)
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Configure columns and rows in main_frame
        self.main_frame.grid_columnconfigure(2, weight=1)  # For spacing between entry and active downages

        # Left frame for entering new downtime
        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.grid(row=0, column=0, padx=50, pady=10, sticky=N)

        # Divider between left and right
        self.divider = ttk.Separator(self.main_frame, orient=VERTICAL)
        self.divider.grid(row=0, column=1, padx=20, pady=10, sticky="ns")

        # Right frame for active downtimes, expanding to take up available space
        self.right_frame = ttk.Frame(self.main_frame)
        self.right_frame.grid(row=0, column=2, padx=50, pady=10, sticky="nsew")

        # Button to open the display window, moving it to its own row to avoid overlap
        self.viewer_button = ttk.Button(self.main_frame, text="Open Viewer", bootstyle="info", command=self.open_viewer)
        self.viewer_button.grid(row=0, column=2, padx=10, pady=10, sticky="ne")

        self.populate_left_frame()
        self.populate_right_frame()

    def populate_left_frame(self): 
        # Title for the left frame
        self.entry_label = ttk.Label(self.left_frame, text="Enter New Downage", bootstyle="primary", font = header_font)
        self.entry_label.grid(row=0, column=0, pady=20)

        # Name input
        self.name_label = ttk.Label(self.left_frame, text="Operator Name:", font = entry_font)
        self.name_label.grid(row=1, column=0, sticky=W)
        self.name_entry = ttk.Entry(self.left_frame, width=entry_width)
        self.name_entry.grid(row=2, column=0, pady=5)

        # Production line / area input
        self.line_label = ttk.Label(self.left_frame, text="Prod. Line / Area:", font = entry_font)
        self.line_label.grid(row=3, column=0, sticky=W)
        self.line_dropdown = ttk.Combobox(self.left_frame, values=self.line_options, width = 43)
        self.line_dropdown.grid(row=4, column=0)

        # equipment name
        self.eqname_label = ttk.Label(self.left_frame, text="Equipment Name:", font = entry_font)
        self.eqname_label.grid(row=5, column=0, sticky=W)
        self.eqname_entry = ttk.Entry(self.left_frame, width=entry_width)
        self.eqname_entry.grid(row=6, column=0, pady=5)

        # equipment id
        self.eqid_label = ttk.Label(self.left_frame, text="Equipment ID:", font = entry_font)
        self.eqid_label.grid(row=7, column=0, sticky=W)
        self.eqid_entry = ttk.Entry(self.left_frame, width=entry_width)
        self.eqid_entry.grid(row=8, column=0, pady=5)

        # Details input
        self.details_label = ttk.Label(self.left_frame, text="Details:", font = entry_font)
        self.details_label.grid(row=9, column=0, sticky=W)
        self.details_entry = ttk.Entry(self.left_frame, width=entry_width)
        self.details_entry.grid(row=10, column=0, pady=5)

        # Submit button
        self.submit_button = ttk.Button(self.left_frame, text="Submit", bootstyle="success", command=self.submit)
        self.submit_button.grid(row=11, column=0, padx = 20, pady=20)

    def populate_right_frame(self):
        # Title for the right frame
        self.active_label = ttk.Label(self.right_frame, text="Active Downages", bootstyle="primary", font = header_font)
        self.active_label.grid(row=0, column=0, pady=20, padx = 50)

        self.actives_frame = ttk.Frame(self.right_frame)
        self.actives_frame.grid(row=1, column=0, sticky=N)
        self.update_actives()

    def update_actives(self):
        self.dt_list = [Downage(name, location, eqname, eqid, details, id, timestamp, emails_sent) 
                        for id, name, location, eqname, eqid, details, timestamp, emails_sent, _, _ in self.db_instance.get_all_unresolved()]
        self.dt_ids = [d.id for d in self.dt_list]

        if self.dt_ids != self.id_checklist or self.update_counter >= 300:
            self.update_counter = 0
            self.id_checklist = [d.id for d in self.dt_list]
            for widget in self.actives_frame.winfo_children():
                widget.destroy()

            for row, downage in enumerate(self.dt_list):
                self.create_active_downtime(self.actives_frame, downage, row)

        self.update_counter += 1
        self.root.after(200, self.update_actives)

    def create_active_downtime(self, parent, downage, row):
        #determine Icon color based on time elapsed

        icon_color = 'Yellow'

        if downage.elapsed_time() > 7200:
            icon_color = 'Red'
        elif downage.elapsed_time() > 1800:
            icon_color = 'Orange'

        # Create frame for downtime
        active_downtime = ttk.Frame(parent, style='ActiveFrame.TFrame')
        active_downtime.grid(row=row + 1, column=0, pady=10, sticky=W + E)

        # Disable the frame's ability to shrink
        active_downtime.grid_propagate(False)
        # Set the desired width and height
        active_downtime.config(width=450, height = 90)

        # Circular icon
        icon_label = ttk.Label(active_downtime, text="●", style = icon_color + 'Icon.TLabel', bootstyle=icon_color)
        icon_label.grid(row=0, column=0, padx=20, pady=5)
 
        # Downtime details (line and time elapsed)
        downtime_label = ttk.Label(active_downtime, text=f"{downage.location}\n{downage.elapsed_time_string()}", style = 'DownageLabel.TLabel')
        downtime_label.grid(row=0, column=1, padx=(0,20), pady=5)

        def resolve_downtime():
            print(downage)
            self.db_instance.resolve_downtime(downage.id)

        # Resolve and alert buttons
        resolve_button = ttk.Button(active_downtime, text="Resolve", bootstyle="danger-outline", command=resolve_downtime)
        resolve_button.grid(row=0, column=2, padx=(10,10), sticky=E)

        alert_button = ttk.Button(active_downtime, text="Alert", bootstyle="warning-outline")
        alert_button.grid(row=0, column=3, padx=(0,10), sticky=E)

        info_button = ttk.Button(active_downtime, text="Info", bootstyle="info-outline", command = lambda: info_window(downage))
        info_button.grid(row=0, column=4, padx=(0,20), sticky=E)

        # for col in range(4):
        #     active_downtime.grid_columnconfigure(col, weight=1)

    def submit(self):
        name = self.name_entry.get()
        line = self.line_dropdown.get()
        eqname = self.eqname_entry.get()
        eqid = self.eqid_entry.get()
        details = self.details_entry.get()

        # Create a new Downage object
        new_downage = Downage(name, line, eqname, eqid, details)
        self.db_instance.add_downtime(new_downage)
        self.clear_fields()

    def open_viewer(self):
        downtime_viewer_window = DowntimeViewer(self.db)
        downtime_viewer_window.start()

    def clear_fields(self):
        self.name_entry.delete(0, ttk.END)
        self.line_dropdown.set('')
        self.eqname_entry.delete(0, ttk.END)
        self.eqid_entry.delete(0, ttk.END)
        self.details_entry.delete(0, ttk.END)

    def start(self):
        self.root.mainloop()
