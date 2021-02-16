# lecture 81
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text="Hello, World!")
name.pack()

# get the layout of a style class:
# TLabel layout: Label.border <- Label.padding <- Label.label
print(style.theme_use())
print(style.layout("TLabel"))

# print the customisable option of each property in TLabel class layout
print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

# retrieve values of existing properties:
# we pass the property and not an element like Label.border
# because if several elements share a property of the same name,
# the values are similar in all elements
print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))

# switching to "clam" theme
style.theme_use("clam")
print(style.theme_use())

print(style.layout("TLabel"))

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))

# configure clam TLabel border element:
style.configure("TLabel", bordercolor="#f00")  # '#f00' = red
style.configure("TLabel", borderwidth=20)
# some themes don't let us configure certain properties,
# for example clam doesnt allow a border of more than 2 pixels
style.configure("TLabel", relief="solid")  # in order for the border to appear

root.mainloop()
