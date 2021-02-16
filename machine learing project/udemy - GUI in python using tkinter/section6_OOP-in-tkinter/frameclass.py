import tkinter as tk
from tkinter import ttk

class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello, World!")

        #instantiate our costume frame class:
        UserInputFrame(self).pack()

class UserInputFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)

        self.user_input = tk.StringVar()

        label = ttk.Label(self, text="enter your name:")
        entry = ttk.Entry(self, textvariable=self.user_input)
        button = ttk.Button(self,text="greet",command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        button.pack(side="left")

    def greet(self):
        print(f"hello, {self.user_input.get()}")


root = HelloWorld()
root.mainloop()