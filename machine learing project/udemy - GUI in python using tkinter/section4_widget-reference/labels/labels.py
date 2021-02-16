import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Labels!")

# using PIL to open the image:
image = Image.open("mypic.jpeg").resize((64, 64))
photo = ImageTk.PhotoImage(image)

# adding a photo to the labael
label = ttk.Label(root, text="Hello, World!", image=photo, padding=20, compound="right")
# compound combines txt and image in the label - it takes the posiztion of the picture relative to the text: right, left, top, buttom, center
label.config(font=("Sego UI", 20))
# set font attr: a tupple of font name and size
label.pack()

# label["image"] = photo #changing a photo in a label

# ----------------------------------------------------------------------------
greeting = tk.StringVar()

label2 = ttk.Label(root, padding=10, textvariable=greeting)  # set the text of a label using a var
label2.pack()

greeting.set("Hello there!")  # enables to edit the text later on in the code

root.mainloop()
