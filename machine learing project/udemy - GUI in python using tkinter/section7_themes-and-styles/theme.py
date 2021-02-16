# lecture 78
import tkinter as tk
from tkinter import ttk


def greet(*args):
    print(f"Hello, {user_name.get()}!")


#           --root--
root = tk.Tk()
root.resizable(False, False)
root.title("Greeter")

#           --style:--

style = ttk.Style(root) # Pass in which application this style is for.

# get available theme:
print(style.theme_names())
# print current theme, can be used to set theme
print(style.theme_use())

#           --main frame--
main = ttk.Frame(root, padding=(40, 20))
main.grid()

user_name = tk.StringVar()

#           --widgets:--
# name_label
name_label = ttk.Label(main, text="Name:")
name_label.grid(row=0, column=0, padx=(0, 10))

# name_entry
name_entry = ttk.Entry(main, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1, padx=10)
name_entry.focus()

# greet_button
greet_button = ttk.Button(main, text="Greet", command=greet)
greet_button.grid(row=0, column=2, sticky="EW", padx=10)

root.mainloop()
