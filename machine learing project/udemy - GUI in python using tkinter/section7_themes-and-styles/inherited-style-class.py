# lecture 82
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

# setting an inherited style, with the wanted configuration
style.configure("CustomEntryStyle.TEntry", padding=20)

name = ttk.Label(root, text="Hello, World!")
entry = ttk.Entry(root, width=15)

#                   custom-name.where-to-inherit-from
entry["style"] = "CustomEntryStyle.TEntry"

name.pack()
entry.pack()

entry2 = ttk.Entry(root, width=15, style="CustomEntryStyle.TEntry")
entry2.pack()

root.mainloop()
