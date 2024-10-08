import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class DowntimeDisplay:
    def __init__(self, db):
        self.db = db
        self.root = ttk.Window(themename="darkly")  # Another theme, e.g., "darkly"
        self.root.title("Downtime Display")

        self.display_button = ttk.Button(self.root, text="Show Downtime", bootstyle="info", command=self.show_downtime)
        self.display_button.pack(padx=10, pady=10)

        self.output = ttk.Text(self.root)
        self.output.pack(padx=10, pady=10)

    def show_downtime(self):
        downtimes = self.db.get_all_downtime()
        self.output.delete(1.0, "end")
        for downtime in downtimes:
            self.output.insert("end", f"{downtime}\n")

    def start(self):
        self.root.mainloop()
