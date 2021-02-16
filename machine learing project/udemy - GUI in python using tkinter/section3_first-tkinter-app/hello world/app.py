#Section 3: Creating Your First Tkinter App: lecture 45

import tkinter as tk
from tkinter import ttk

#creating a main window object:

#creating a Tk object
root = tk.Tk()

#creating a lable in our window: ttk.Label(parent, option...)
#.pack() displays the label on the window
ttk.Label(root, text="Hello, world!", padding=(30,10)).pack()

#running the window:
#mainLoop() enters a while loop that resumes until the window is closed
root.mainloop()