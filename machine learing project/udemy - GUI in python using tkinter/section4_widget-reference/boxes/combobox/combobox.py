import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("check buttons!")

selected_weekday = tk.StringVar()


# defining the function to be called upon selection
def handle_selection(event):
    print(f"Today is: {selected_weekday.get()}")
    print("But we're going to change it to Friday")
    selected_weekday.set(
        "Friday")  # if we set to a value that is not in the values tupple it will be added to the combobox
    print(f"selected is: {weekday.get()} which at idx {weekday.current()} in the values tupple")


# define a combobox:
weekday = ttk.Combobox(
    root,
    textvariable=selected_weekday,
    values=("Sunday", "Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday"),
    state="readonly"
)

# binding the combobox to event and fucntion:
# the bind will call the handle func with the given event
weekday.bind("<<ComboboxSelected>>", handle_selection)

weekday.pack()

root.mainloop()

print(f"exit program, {selected_weekday.get()} was selected")
