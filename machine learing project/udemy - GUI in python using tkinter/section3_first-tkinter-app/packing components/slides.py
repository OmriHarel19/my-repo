#Section 3: Creating Your First Tkinter App: lecture 48
import tkinter as tk

root = tk.Tk()
#controling window size:
root.geometry("600x400")

#creating and packing our lables:
#using tk.Label here and not ttk.Label - for this purpose there is no difference

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

#ipadx/idpady - internal pad of the lable

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(side="top", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_3 = tk.Label(root, text="Rectangle 3", bg="black", fg="white")
rectangle_3.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_4 = tk.Label(root, text="Rectangle 4", bg="blue", fg="white")
rectangle_4.pack(side="top", ipadx=10, ipady=10, fill="both", expand=True)
'''
'''
root.mainloop()