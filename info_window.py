import ttkbootstrap as ttk
from center_window import center_window

def info_window(downage):
        info_window = ttk.Toplevel()
        info_window.title("Downage Information")

        center_window(info_window, 360, 380)
        
        # Display downtime information as labels
        fields = {
            "ID": downage.id,
            "Name": downage.name,
            "Location": downage.location,
            "Equipment Name": downage.eqname,
            "Equipment ID": downage.eqid,
            "Details": downage.details,
            "Timestamp": downage.timestamp,
            'Emails Sent': 'No' if downage.emails_sent == 0 else 'Yes',
            "Resolved": 'No' if downage.resolved == 0 else 'Yes',
            "Time Resolved": downage.time_resolved,
            "Time to Resolve": downage.time_to_resolve
        }
        
        for idx, (key, value) in enumerate(fields.items()):
            ttk.Label(info_window, text=f"{key}:").grid(row=idx, column=0, sticky="w", padx=10, pady=5)
            ttk.Label(info_window, text=value).grid(row=idx, column=1, sticky="w", padx=10, pady=5)
        
        # Add a close button
        close_button = ttk.Button(info_window, text="Close", command=info_window.destroy)
        close_button.grid(row=len(fields), column=0, columnspan=2, pady=10)