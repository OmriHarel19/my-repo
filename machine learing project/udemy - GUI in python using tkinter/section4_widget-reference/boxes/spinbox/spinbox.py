import tkinter as tk
from tkinter import ttk


# --------------------------------------------------

def handle_spinbox():
    print(f"selected: {initial_value.get()}")


# --------------------------------------------------


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Spin Box!")

initial_value = tk.IntVar(value=0)

# define a spinbox:
# from_ and to define e the boundary of values the spinbox can have
# instead of defining upper and lower limit we can define a tuple of values in the 'values' attr
# wrap - a bool that if set true the value on the spin box resets when we reach the limit,
# ex: when getting to the value 30 and trying to increase it will return to 0
spin_box = ttk.Spinbox(
    root,
    values=tuple([i for i in range(0, 31, 5)]),
    textvariable=initial_value,
    wrap=False
)

spin_box.pack()

# create a display button:
display_button = ttk.Button(root, text="print selection", command=handle_spinbox)

display_button.pack()

root.mainloop()
