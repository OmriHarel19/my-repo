import tkinter as tk
import tkinter.font as font
from tkinter import ttk


# window class:
class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")

        # a dictionary of all frames:
        self.frames = dict()

        # main container:
        container = ttk.Frame(self)
        container.grid(row=0, column=0, padx=60, pady=30, sticky="EW")

        # creating all frames:
        for FrameClass in (MetersToFeet, FeetToMeters):  # running over our classes
            frame = FrameClass(container, self)  # creating the frame
            self.frames[FrameClass] = frame  # adding to frames dict
            frame.grid(row=0, column=0, sticky="NSEW")  # place frames in the same row and col

        # showing wanted frame:
        self.show_frame(MetersToFeet)

    # when putting two widgets in the same place, by default the last one added is going to be displayed
    # tkraise() allows us to select which widget will be displayed on top of the others
    def show_frame(self, container):
        # gets a container frame and raises it - showing it on the window
        # creating key binds for this frame

        # get the wanted frame to be raised
        frame = self.frames[container]

        # bind keybinds to the main window (self)
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)

        # raise frame
        frame.tkraise()


# MetersToFeet class:
class MetersToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        # container - the container in which the frame is going to be
        # controller - our window, the object that controls which frame is going to be shown
        super().__init__(container, **kwargs)

        #                       --class vars--

        # define entry content var:
        self.meters_value = tk.StringVar()
        # define feet display var:
        self.feet_value = tk.StringVar(value="feet shown here")

        #                       --widgets--
        # meters labels:
        meters_label = ttk.Label(self, text="Meters:")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value,
                                 font=("Segoe UI", 12))  # passing our Stringvar to hold the entry val
        # feet labels:
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable=self.feet_value)

        # convert button:
        calc_button = ttk.Button(self, text="convert", command=self.calculate)

        # switch button:
        switch_page_button = ttk.Button(
            self,
            text="switch to feet conversion:",
            command=lambda: controller.show_frame(FeetToMeters)
        )

        #                       --layout--
        meters_label.grid(row=0, column=0, sticky="w")  # sticking to the left
        meters_input.grid(row=0, column=1, sticky="ew")  # stick left and right
        meters_input.focus()

        feet_label.grid(row=1, column=0, sticky="w")  # sticking to the left
        feet_display.grid(row=1, column=1, sticky="ew")  # stick left and right

        calc_button.grid(row=2, column=0, columnspan=2, sticky="ew")
        switch_page_button.grid(row=3, column=0, columnspan=2, sticky="ew")

        # using winfo_children() to configure all widget padding value in main
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def calculate(self, *args):
        try:
            meters = float(self.meters_value.get())  # remember to convert str to float
            feet = meters * 3.28084
            self.feet_value.set(str(f"{feet:.3f}"))
        except ValueError:  # raised when the entry is empty
            pass


# FeetToMeters class:
class FeetToMeters(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        #                       --class vars--

        # define entry content var:
        self.meters_value = tk.StringVar(value="meters shown here")
        # define feet display var:
        self.feet_value = tk.StringVar()

        #                       --widgets--
        # feet labels:
        feet_label = ttk.Label(self, text="Feet:")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value,
                               font=("Segoe UI", 12))  # passing our Stringvar to hold the entry val
        # meters labels:
        meters_label = ttk.Label(self, text="Meters:")
        meters_display = ttk.Label(self, textvariable=self.meters_value)

        # convert button:
        calc_button = ttk.Button(self, text="convert", command=self.calculate)

        # switch button:
        switch_page_button = ttk.Button(
            self,
            text="switch to meters conversion:",
            command=lambda: controller.show_frame(MetersToFeet)
        )

        #                       --layout--
        feet_label.grid(row=0, column=0, sticky="w")  # sticking to the left
        feet_input.grid(row=0, column=1, sticky="ew")  # stick left and right
        feet_input.focus()

        meters_label.grid(row=1, column=0, sticky="w")  # sticking to the left
        meters_display.grid(row=1, column=1, sticky="ew")  # stick left and right

        calc_button.grid(row=2, column=0, columnspan=2, sticky="ew")
        switch_page_button.grid(row=3, column=0, columnspan=2, sticky="ew")

        # using winfo_children() to configure all widget padding value in main
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())  # remember to convert str to float
            meters = feet / 3.28084
            self.meters_value.set(str(f"{meters:.3f}"))
        except ValueError:  # raised when the entry is empty
            pass


# --------code--------------------------------------


# create window
root = DistanceConverter()

# adjusting font size - doesnt change entry font size
font.nametofont("TkDefaultFont").configure(size=12)

# expand first col:
root.columnconfigure(0, weight=1)

root.mainloop()
