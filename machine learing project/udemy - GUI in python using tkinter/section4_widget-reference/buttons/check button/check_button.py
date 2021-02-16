import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("check buttons!")

selected_option = tk.StringVar()
button_text = tk.StringVar(value="hello!")

def print_current_option():
    print(selected_option.get())

#create a check button:
check_button = ttk.Checkbutton(
    root,
    textvariable=button_text,
    variable=selected_option,
    command=print_current_option,
    onvalue="on",
    offvalue="off"
)
check_button.pack()


root.mainloop()