
# Font settings
font_option = "Microsoft YaHei UI"
header_font = (font_option, 24)
entry_font = (font_option, 14)
entry_width = 45
icon_size = 48
theme = "litera"

def set_custom_styles(self):
    self.style.configure('DownageLabel.TLabel',
                    font=entry_font,
                    background = self.style.colors.secondary
                    )
    
    self.style.configure('RedIcon.TLabel',
                    font=("", icon_size),
                    foreground = self.style.colors.danger,
                    background = self.style.colors.secondary
                    )
    
    self.style.configure('OrangeIcon.TLabel',
                    font=("", icon_size),
                    foreground = self.style.colors.warning,
                    background = self.style.colors.secondary
                    )
    
    self.style.configure('YellowIcon.TLabel',
                    font=("", icon_size),
                    foreground = 'yellow',
                    background = self.style.colors.secondary
                    )