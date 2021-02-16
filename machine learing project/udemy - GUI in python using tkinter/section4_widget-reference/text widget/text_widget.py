import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# ---------------------------------------------

def print_content():
    text_content = text.get("2.0", "end")
    print(f"added content:\n {text_content}")


# ---------------------------------------------

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("text widget!")

# define a text box:
# height = number of rows in the textbox
text = tk.Text(root, height=8)
text.pack()

# insert text to the text box:
# "1.0" - indicates the positions where to insert the text as follows:
# row.col, (rows begin at idx =1 while cols begin at idx = 0)
text.insert("1.0", "please enter a comment...")

# disable/enable text box:
text["state"] = "normal"  # or "disabled"

# retrieve data from text box:
# text.get(start_point,end_point)
text_content = text.get("1.0", "end")  # end will find the end for you
print(f"init content: {text_content}")

print_text_button = ttk.Button(root, text="click to print the text content",
                               command=print_content)
print_text_button.pack()
root.mainloop()
