import tkinter as tk
from tkinter import ttk

#------------------------------------------------

def handle_scale_event(event):
    label_value.set(str(scale.get()))

#------------------------------------------------

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("check buttons!")


current_value = tk.DoubleVar()
label_value = tk.StringVar(value="0")

scale = ttk.Scale(
    root,
    orient="horizontal",
    from_=0,
    to=10,
    command=handle_scale_event,
    variable=current_value
)

scale.pack(fill="x")

display_label = ttk.Label(root, textvariable=label_value)

display_label.pack()

root.mainloop()