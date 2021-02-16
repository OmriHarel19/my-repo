import tkinter as tk
from tkinter import ttk
from collections import deque
from section8_pomodoro_timer.frames import Timer, Settings

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


# main window class
class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Pomodoro Timer")

        #           --class properties--

        # self.timer_time_settings = {time_setting_name:time}
        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)
        self.frames = dict()

        # making the app-main window responsible for timing schedule and time setting
        # while the timer frame is in charge of displaying the timer
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro",
                            "Long Break"]  # a list of timer operation order
        self.timer_schedule = deque(self.timer_order)  # behave like a Queue, we can rotate elements around

        #           ----setting style----

        style = ttk.Style(self)
        style.theme_use("clam")

        # name.TClass - name style inherits the style of Class, while configuring one of its properties
        style.configure("Timer.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)

        style.configure(
            "TimerText.TLabel",  # a style configure for a specific element
            background=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            font='Courier 38'
        )
        style.configure(
            "LightText.TLabel",  # a more generic configure, can be used for many elements
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.configure(
            "PomodoroButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT
        )

        # styling the button according to events:
        style.map(
            "PomodoroButton.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]  # active == hover
        )

        # since self is a tk obj it doesnt have a style property, so we need to set manually
        self["background"] = COLOUR_PRIMARY

        #       ----window layout & configuration----

        #           --grid configure--
        self.columnconfigure(0, weight=1)  # to center our main frame
        self.rowconfigure(1, weight=1)  # expand 2nd row to push first up (this happens by default)

        #           --main container frame--
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)  # expanding 1st col

        #           --timer frame--
        timer_frame = Timer(container, self, lambda: self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky="NESW")  # take all available space

        #           --setting frame
        settings_frame = Settings(container, self, lambda: self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky="NESW")  # take all available space

        # add frames to frame dict
        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame

        self.show_frame(Timer)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


app = PomodoroTimer()
app.mainloop()
