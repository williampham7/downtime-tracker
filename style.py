
# Font settings
font_option = "Microsoft YaHei UI"
header_font = (font_option, 24)
entry_font = (font_option, 14)
entry_width = 45
icon_size = 48
theme = "litera"
light_gray = '#d9d9d9'

def set_custom_styles(self):
    self.style.configure('ActiveFrame.TFrame',
                    background = light_gray
                    )

    self.style.configure('DownageLabel.TLabel',
                    font=entry_font,
                    background = light_gray
                    )
    
    self.style.configure('RedIcon.TLabel',
                    font=("", icon_size),
                    foreground = self.style.colors.danger,
                    background = light_gray
                    )
    
    self.style.configure('OrangeIcon.TLabel',
                    font=("", icon_size),
                    foreground = self.style.colors.warning,
                    background = light_gray
                    )
    
    self.style.configure('YellowIcon.TLabel',
                    font=("", icon_size),
                    foreground = 'yellow',
                    background = light_gray
                    )
