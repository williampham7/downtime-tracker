def center_window(window, x, y):
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            main_corner_x = (screen_width // 2) - (x // 2)
            main_corner_y = (screen_height // 2) - (y // 2) - screen_height // 20
            main_geometry = (f"{x}x{y}+{main_corner_x}+{main_corner_y}")
            window.geometry(main_geometry)