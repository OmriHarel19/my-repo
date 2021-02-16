import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("check buttons!")

storage_variable = tk.StringVar()

#creating our radio buttons:
#value = the value the is going to placed in variable upon selection
#all buttons have the same variable -> this is what connects them as radio buttons
option_one = ttk.Radiobutton(
    root,
    text="option 1",
    variable=storage_variable,
    value="First option"
)

option_two = ttk.Radiobutton(
    root,
    text="option 2",
    variable=storage_variable,
    value="Second option"
)

option_three = ttk.Radiobutton(
    root,
    text="option 3",
    variable=storage_variable,
    value="Third option"
)

option_one.pack()
option_two.pack()
option_three.pack()

root.mainloop()