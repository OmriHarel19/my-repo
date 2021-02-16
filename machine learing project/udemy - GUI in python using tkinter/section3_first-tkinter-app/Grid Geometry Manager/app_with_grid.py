# Section 3: Creating Your First Tkinter App: lecture 46 - 47
# upgrading the app: replacing pack with grid: lecture 51
import tkinter as tk
from tkinter import ttk

# -------------------------------------------------------------------
try:
    from ctypes import windll

    windll.shchore.SetProcessDpiAwareness(1)
except:
    pass


# ---------func section----------------------------------------------

# command func for our button
def greet():
    print(f"hello, {user_name.get() or 'World'}!")


# creating root
root = tk.Tk()
root.title("Greeter")

root.columnconfigure(0, weight=1)
# weight - a measure for how much space the row/col is going to take. by default is 0
# this measure is relative - if one col has a weight of 2 and another a weight of 1: then the first will take twice as much space

# creating a StringVar that will contain the string from the entry field
user_name = tk.StringVar()

# creating input frame:
input_frame = ttk.Frame(root, padding=(10, 5, 10, 0))  # padding 4 values: left,top,right,bottom
input_frame.grid(row=0, column=0,
                 sticky="EW")  # using a grid in root, placing the first frame at the first row nad col within root

# setting the input_frame columns with equal weights of one so the take equals amount of space in their row
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

# creating a label:
name_label = ttk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=(0, 10))  # using a grid in input_frame, placing the first label at the first row and col in  input_frame
# creating an Entry
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)  # width is a measure of charcaters, not pixels
name_entry.grid(row=0, column=1)  # placing the second label at the first row and second col in input_frame
name_entry.focus()  # enables us to use the entry as soon as the app starts

# making the buttons expand in respective columns

# creating buttons frame:
buttons = ttk.Frame(root, padding=(20, 10))  # padding 2 values: left/right, top/bottom
buttons.grid(row=1, column=0,
             sticky="EW")  # make the frame stick to the "east west" exis and take all of the available space in that exis

# setting the button columns with equals weights of one so the take equals amount of space in their row
buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)

# creating a button:
# we make the buttons sticky in the "eat west" axis so that they'll expand as much they can on the horizontal line
greet_button = ttk.Button(buttons, text="greet", command=greet)
# adding the button to the frame with .grid()
greet_button.grid(row=0, column=0, sticky="EW")

# creating a second button:
# root.destroy() - cloeses the window
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

root.mainloop()
