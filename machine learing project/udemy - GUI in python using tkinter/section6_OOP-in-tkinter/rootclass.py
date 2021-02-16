import tkinter as tk
from tkinter import ttk

class HelloWorld(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Hello, world!")

        ttk.Label(self,text="Hello, world!").pack()

root = HelloWorld()
root.mainloop()