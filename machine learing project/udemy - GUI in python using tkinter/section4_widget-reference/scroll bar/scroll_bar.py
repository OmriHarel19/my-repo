import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("scroll bars")

#configaring first row and col of root to take up all available space
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

#text widget:
text = tk.Text(root,height=8)
text.grid(row=0, column=0, sticky="ew")
text.insert("1.0", "Please enter a comment...")

#scroll bar:

#binding the scroll to the text box: scroll bar is modifying the property
# in the text box that we want to control: in this case text.yview
text_scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
text_scroll.grid(row=0,column=1, sticky="ns")
#binding the text box to the scroll:
text["yscrollcommand"] = text_scroll.set

root.mainloop()