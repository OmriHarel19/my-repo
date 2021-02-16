import tkinter as tk
from tkinter import ttk


class Settings(ttk.Frame):
    def __init__(self, parent, controller, show_timer):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        #       --setting frame--
        settings_container = ttk.Frame(
            self,
            padding=(30, 15, 30, 15),
            style="Background.TFrame"
        )

        settings_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(1, weight=1)

        #       --settings--

        # pomodoro label & spinbox:
        pomodoro_label = ttk.Label(
            settings_container,
            text="Pomodoro: ",
            style="LightText.TLabel"
        )
        pomodoro_label.grid(row=0, column=0, sticky="W")

        pomodoro_input = tk.Spinbox(
            settings_container,
            from_=0, to=120,
            increment=1,
            justify="center",  # values are going to be centered
            textvariable=controller.pomodoro,  # value selected in the spinbox goes to PomodoroTimer.pomodoro
            width=10,
            state="readonly"
        )
        pomodoro_input.grid(row=0, column=1, sticky="EW")
        pomodoro_input.focus()  # can be changed as soon as it is created

        # long break label & spinbox:
        long_break_label = ttk.Label(
            settings_container,
            text="long_break: ",
            style="LightText.TLabel"
        )
        long_break_label.grid(row=1, column=0, sticky="W")

        long_break_input = tk.Spinbox(
            settings_container,
            from_=0, to=60,
            increment=1,
            justify="center",  # values are going to be centered
            textvariable=controller.long_break,  # value selected in the spinbox goes to PomodoroTimer.long_break
            width=10,
            state="readonly"
        )
        long_break_input.grid(row=1, column=1, sticky="EW")
        long_break_input.focus()  # can be changed as soon as it is created

        # short break label & spinbox:
        short_break_label = ttk.Label(
            settings_container,
            text="short_break: ",
            style="LightText.TLabel"
        )
        short_break_label.grid(row=2, column=0, sticky="W")

        short_break_input = tk.Spinbox(
            settings_container,
            from_=0, to=30,
            increment=1,
            justify="center",  # values are going to be centered
            textvariable=controller.short_break,  # value selected in the spinbox goes to PomodoroTimer.short_break
            width=10,
            state="readonly"
        )
        short_break_input.grid(row=2, column=1, sticky="EW")
        short_break_input.focus()  # can be changed as soon as it is created

        # setting padding:
        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        #       -- switch to timer button--

        # button frame:
        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(row=1, column=0, sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        # button:
        timer_button = ttk.Button(
            button_container,
            text="<-Back",
            command=show_timer,
            cursor="hand2",
            style="PomodoroButton.TButton"
        )
        timer_button.grid(row=0, column=0, sticky="EW", padx=2)
