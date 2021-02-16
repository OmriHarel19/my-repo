#Section 3: Creating Your First Tkinter App: lecture 46 - 47
#upgrading the app with frames: lecture 50
import tkinter as tk
from tkinter import ttk

#---------func section----------------------------------------------

#command func for our button
def greet():
    print(f"hello, {user_name.get() or 'World'}!")

#-------------------------------------------------------------------
#app structure:
#root window contains two frames that are top aligned
#the first contains the name label and the enttry widget
#the secodn contains the greet and quit buttons
#the frames allows us to orgenzie our app and place the widget more freely to our choice
#-------------------------------------------------------------------

#creating root
root = tk.Tk()
root.title("Greeter")

#creating a StringVar that will contain the string from the entry field
user_name = tk.StringVar()

#creating input frame:
input_frame = ttk.Frame(root, padding=(10,20,10,0)) #padding 4 values: left,top,right,bottom
input_frame.pack(fill="both")

#creating a label:
name_label = ttk.Label(input_frame, text="Name:")
name_label.pack(side="left",padx=(0,10))
#creating an Entry
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name) #width is a measure of charcaters, not pixels
name_entry.pack(side="left")
name_entry.focus() #enables us to use the entry as soon as the app starts


#creating buttons frame:
buttons = ttk.Frame(root,padding=(20,10)) #padding 2 values: left/right, top/bottom
buttons.pack(fill="both")

#creating a button:
greet_button = ttk.Button(buttons, text="greet", command=greet)
#adding the button to the frame with .pack()
greet_button.pack(side="left",fill="x", expand=True)

#creating a second button:
#root.destroy() - cloeses the window
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.pack(side="left",fill="x",expand=True)


root.mainloop()