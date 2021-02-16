# lecture 79-80
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam")

name = ttk.Label(root, text="Hello, world!", style="TLabel")  # can pass the wanted style class
entry = ttk.Entry(root, width=15)
name.pack()

# ** tk widgets don't accept a style arg, only ttk

# check label's style property:
print(name["style"])
# check style class name:
print(name.winfo_class())  # class: TLabel

# configure style:
style.configure("TLabel", font=("Segoe UI", 20))

root.mainloop()
