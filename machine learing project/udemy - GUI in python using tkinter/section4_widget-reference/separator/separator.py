import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("separators")

#configaring first row and col of root to take up all available space
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

#setting to labels with a separator:
ttk.Label(root,text="Hello world", padding=20, background="green").pack()

#by default separators are one pixel long, we use fill in the wanted axis
ttk.Separator(root, orient="horizontal").pack(fill="x")

ttk.Label(root,text="Hello world", padding=20).pack()

root.mainloop()