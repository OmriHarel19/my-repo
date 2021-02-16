import tkinter as tk
from tkinter import ttk


# --------------------------------------

# handle fucntion:
def handle_selection_change(event):
    selected_indices = langs_select.curselection()  # returns a list of indices
    for i in selected_indices:
        print(f"{langs_select.get(i)} language selected")  # get(i) - gets element by idx


# ------------------------------------------

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("check buttons!")

# configuring first row and col of root to take up all available space
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# creating a main frame
main = ttk.Frame(root)
main.grid(row=0, column=0)

# setting vars:
programing_languages = ("C", "python", "java", "asm", "sql", "JS", "C++")
langs = tk.StringVar(value=programing_languages)

# defining a listbox:
# listvariable - tells tk to extract the data from the tuple
# height - number of values to be shown at any time
# selectmode= "extended" - allows the selection of multiple options, "browse" for single selection
langs_select = tk.Listbox(
    main,
    listvariable=langs,
    height=6,
    selectmode="extended"
)

# binding the listbox:
langs_select.bind("<<ListboxSelect>>", handle_selection_change)

langs_select.grid(row=0, column=0)

# create a scroll:
scroll = ttk.Scrollbar(main, orient="vertical", command=langs_select.yview)
scroll.grid(row=0, column=1, sticky="ns")
langs_select["yscrollcommand"] = scroll.set

root.mainloop()
