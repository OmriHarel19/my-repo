# lecture 83
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam")

# need to remember there are theme limitations! some themes don't allow certain changes

# create custom style options on specific states using map
style.map(
    "CustomButton.TButton",
    # each tuple is (states/events(can be more than one), new property value)
    foreground=[("pressed", "red"), ("active", "white")],
    background=[("pressed", "!disabled", "black"), ("active", "black")],
    font=[("pressed", ("TkDefaultFont", 15))]
)

name = ttk.Label(root, text="Hello, World!")
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text="Press me.", style="CustomButton.TButton")

name.pack()
entry.pack()
button.pack()


root.mainloop()
