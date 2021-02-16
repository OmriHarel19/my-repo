import tkinter as tk
import tkinter.font as font
from tkinter import ttk


# -------funcs:---------------------------------------

def calc_feet(*args):
    try:
        meters = float(meters_value.get())  # remember to convert str to float
        feet = meters * 3.28084
        feet_value.set(str(f"{feet:.3f}"))
    except ValueError:  # raised when the entry is empty
        pass


# --------root, main frame and variables--------------------------------------

# create window
root = tk.Tk()
root.title("Distance converter")

# expand first col:
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# adjusting font size - doesnt change entry font size
font.nametofont("TkDefaultFont").configure(size=12)

# define entry content var:
meters_value = tk.StringVar()
# define feet display var:
feet_value = tk.StringVar(value="feet shown here")

# create main frame
main = ttk.Frame(root, padding=(30, 15))
main.grid(row=0, column=0)

# ---------widgets: children of main frame-----------------------------------------

# create widgets:
# meter labels:
meters_label = ttk.Label(main, text="Meters:")
meters_input = ttk.Entry(main, width=10, textvariable=meters_value,
                         font=("Segoe UI", 12))  # passing our Stringvar to hold the entry val
# feet labels:
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, textvariable=feet_value)
# convert button:
calc_button = ttk.Button(main, text="convert", command=calc_feet)

# ------------placing widgets in main frame using grid: -----------------------------

meters_label.grid(row=0, column=0, sticky="w")  # sticking to the left
meters_input.grid(row=0, column=1, sticky="ew")  # stick left and right
meters_input.focus()

feet_label.grid(row=1, column=0, sticky="w")  # sticking to the left
feet_display.grid(row=1, column=1, sticky="ew")  # stick left and right

calc_button.grid(row=2, column=0, columnspan=2, sticky="ew")
# expanding col 0 to occupy the space of two cols 0 and 1
# stick left and right

# ------------using winfo_children()-------------------------------------------------

# using winfo_children() to configure all widget padding value in main
for child in main.winfo_children():
    child.grid_configure(padx=10, pady=10)

# --------------creating keybindings:---------------------------------------------------
# binding to root because we have only one entry field, if we had more and wanted to create keybind just for the entry we could bind it instead
root.bind("<Return>", calc_feet)  # <Return> = enter key press
root.bind("<KP_Enter>", calc_feet)  # <KP_Enter> = enter in numpad key press

root.mainloop()
