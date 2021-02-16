# Section 3: Creating Your First Tkinter App: lecture 49
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# creating a frame in root - our main window
main = ttk.Frame(root)
# the frame is anchored to the left
main.pack(side="left", fill="both", expand=True)

# inside the frame we pack two lables that are anchored to top. they share space only within the main Frame and not root
tk.Label(main, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(main, text="Label top", bg="red").pack(side="top", expand=True, fill="both")
# a third label is placed in root, which shares space with the frame back in main
# result is that both labels in the frame take its entire space, and the frame itself takes the left side of root, splitted equaly with the third label - because they have same expand priority
tk.Label(root, text="Label left", bg="green").pack(
    side="left", expand=True, fill="both"
)

root.mainloop()
