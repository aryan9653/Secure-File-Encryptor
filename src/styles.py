from tkinter import font

# Theme Colors
BG_COLOR = "#2C2F33"
TEXT_COLOR = "#FFFFFF"
BUTTON_COLOR = "#7289DA"
BUTTON_HOVER = "#5B6EAE"
ENTRY_BG = "#23272A"

# Fonts
def get_fonts(root):
    return {
        "title": font.Font(root, family="Arial", size=16, weight="bold"),
        "button": font.Font(root, family="Arial", size=12, weight="bold"),
        "entry": font.Font(root, family="Arial", size=12),
    }
