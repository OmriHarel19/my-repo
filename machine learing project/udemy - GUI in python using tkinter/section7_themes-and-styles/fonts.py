# lecture 84
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
style = ttk.Style(root)

# ** can't use style or style inherited class of the style property
# inside an entry to change its font - only using tkinter.font, or the font property itself

# list of useful default fonts:
# https://github.com/tecladocode/gui-development-tkinter-course/tree/master/section07/07_changing_entry_field_font_with_styles

# doesn't affect entries because it has a different default font
font.nametofont("TkDefaultFont").configure(size=15)
# TkTextFont - default of all text widgets
font.nametofont("TkTextFont").configure(size=15)

# creating a custom font object using tkinter.font:
# special font family names: Helvetica, Times, Courier
warningLabelFont = font.Font(family="Helvetica", size=14, weight="bold")

# create a font obj for a default font:
# we create a copy so that any changes we do on that obj will not affects other widgets
warningLabelFont2 = font.nametofont("TkDefaultFont").copy()
warningLabelFont2.configure(size=20)

# existing fonts in the system:
print(font.families())

name = ttk.Label(root, text="Hello, World!", font=warningLabelFont2)
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text="Press me.")

name.pack()
entry.pack()
button.pack()

root.mainloop()
