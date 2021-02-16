import tkinter as tk
from tkinter import ttk
from section9_chat_app.frames import Chat
import tkinter.font as font

# color values:
COLOUR_LIGHT_BACKGROUND_1 = "#fff"
COLOUR_LIGHT_BACKGROUND_2 = "#f2f3f5"
COLOUR_LIGHT_BACKGROUND_3 = "#e3e5e8"

COLOUR_LIGHT_TEXT = "#aaa"

COLOUR_BUTTON_NORMAL = "#5fba7d"
COLOUR_BUTTON_ACTIVE = "#58c77c"
COLOUR_BUTTON_PRESSED = "#44e378"


class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1200x500")
        self.minsize(800, 500)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.chat_frame = Chat(
            self,
            background=COLOUR_LIGHT_BACKGROUND_1,
            style="Messages.TFrame"
        )

        self.chat_frame.grid(row=0, column=0, sticky="NSEW")


root = Messenger()

# --styling--

# resize font
font.nametofont("TkDefaultFont").configure(size=14)

# change to clam theme
style = ttk.Style(root)
style.theme_use("clam")

# frame styles:
style.configure("Messages.TFrame", background=COLOUR_LIGHT_BACKGROUND_3)
style.configure("Controls.TFrame", background=COLOUR_LIGHT_BACKGROUND_2)

# button styles:
style.configure("SendButton.TButton", borderwidth=0, background=COLOUR_BUTTON_NORMAL)
style.map(
    "SendButton.TButton",
    background=[("pressed", COLOUR_BUTTON_PRESSED), ("active", COLOUR_BUTTON_ACTIVE)],
)

style.configure("FetchButton.TButton", background=COLOUR_LIGHT_BACKGROUND_1, borderwidth=0)

# label styles:
style.configure(
    "Time.TLabel",
    padding=5,
    background=COLOUR_LIGHT_BACKGROUND_1,
    foreground=COLOUR_LIGHT_TEXT,
    font=8
)
style.configure("Message.TLabel", background=COLOUR_LIGHT_BACKGROUND_2)
style.configure("Avatar.TLabel", background=COLOUR_LIGHT_BACKGROUND_3)


root.mainloop()
