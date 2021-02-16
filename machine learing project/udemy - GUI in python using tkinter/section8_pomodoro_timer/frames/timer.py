import tkinter as tk
from tkinter import ttk
from collections import deque


# timer frame class:
class Timer(ttk.Frame):
    def __init__(self, parent, controller, show_settings):
        super().__init__(parent)

        self["style"] = "Background.TFrame"  # because Timer is a ttk obj it has a style attr

        #       --class properties--
        self.controller = controller
        pomodoro_time = int(self.controller.pomodoro.get())
        self.current_time = tk.StringVar(value=f"{pomodoro_time:02d}:00")
        self.current_timer_label = tk.StringVar(
            value=self.controller.timer_schedule[0])  # contains current state of the timer
        self.timer_running = False  # timer starts non-active
        self.start_button, self.stop_button, self.reset_button = None, None, None
        self._timer_decrement_job = None  # creating a private variable

        # style: since Timer class sits in side our main window, the PomodoroTimer class, it has access to all of its
        # style classes

        #       --timer state label--
        timer_description = ttk.Label(
            self,
            textvariable=self.current_timer_label,
            style="LightText.TLabel"
        )
        timer_description.grid(row=0, column=0, sticky="W", padx=(10, 0), pady=(10, 0))  # sticking to left

        #       --switch to settings frame button--
        settings_button = ttk.Button(
            self,
            text="Go to settings:",
            command=show_settings,  # calling PomodoroTimer.show_frame(Settings)
            style="PomodoroButton.TButton",  # style class from super
            cursor="hand2"
        )
        settings_button.grid(row=0, column=1, sticky="E", padx=(10, 0), pady=(10, 0))  # sticking to right

        #       --the timer display--

        # timer frame
        timer_frame = ttk.Frame(self, height="100", style="Timer.TFrame")  # fixed height of 100px
        timer_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="NSEW")

        # timer counter label
        timer_counter = ttk.Label(
            timer_frame,
            textvariable=self.current_time,
            style="TimerText.TLabel"
        )

        # center the timer in the timer frame frame using place: position specified in a fraction
        timer_counter.place(relx=0.5, rely=0.5, anchor="center")

        #       --buttons--

        # button Frame:
        button_container = ttk.Frame(self, padding=10, style="Background.TFrame")
        button_container.grid(row=2, column=0, columnspan=2, sticky="EW")
        button_container.columnconfigure((0, 1, 2), weight=1)  # all cols take equal space

        # start button:
        self.start_button = ttk.Button(
            button_container,
            text="Start",
            command=self.start_timer,
            style="PomodoroButton.TButton",
            cursor="hand2"  # cursor setting when hovering the button
        )

        self.start_button.grid(row=0, column=0, sticky="EW")

        # start button:
        self.stop_button = ttk.Button(
            button_container,
            text="Stop",
            state="disabled",  # starts disabled
            command=self.stop_timer,
            style="PomodoroButton.TButton",
            cursor="hand2"  # cursor setting when hovering the button
        )

        self.stop_button.grid(row=0, column=1, sticky="EW", padx=5)  # padding horizontally on both sides

        # reset button:
        self.reset_button = ttk.Button(
            button_container,
            text="Reset",
            command=self.reset_timer,
            style="PomodoroButton.TButton",
            cursor="hand2"  # cursor setting when hovering the button
        )

        self.reset_button.grid(row=0, column=2, sticky="EW")

    #           --button commands--

    def start_timer(self):
        self.timer_running = True  # set timer state on
        self.start_button["state"] = "disabled"  # disable start button once pressed
        self.stop_button["state"] = "enabled"  # enable stop button

        # call decrement_time
        self.decrement_time()

    def stop_timer(self):
        self.timer_running = False  # set timer state off
        self.stop_button["state"] = "disabled"  # disable stop button once pressed
        self.start_button["state"] = "enabled"  # enable start button

        # terminate decrement_time:
        if self._timer_decrement_job:  # check if job exists
            self.after_cancel(self._timer_decrement_job)  # cancel it
            self._timer_decrement_job = None  # reset variable

    def reset_timer(self):
        self.stop_timer()  # stop timer, disable stop & enable start
        self.controller.timer_schedule = deque(self.controller.timer_order)  # reset timer order
        pomodoro_time = int(self.controller.pomodoro.get())
        self.current_time.set(f"{pomodoro_time:02d}:00")  # reset timer to init value (Pomodoro time)
        self.current_timer_label.set(self.controller.timer_schedule[0])

    #           --timer update--

    def decrement_time(self):
        current_time = self.current_time.get()  # temp var to store cur time

        # check if timer should run, and not reach 0
        if self.timer_running and current_time != "00:00":
            minutes, seconds = current_time.split(":")

            # seconds > 0:
            if int(seconds) > 0:
                seconds = int(seconds) - 1
                minutes = int(minutes)
            # seconds = 0:
            else:
                seconds = 59
                minutes = int(minutes) - 1

            # update time:
            self.current_time.set(f"{minutes:02d}:{seconds:02d}")

            # iterate func using Frame.after
            self._timer_decrement_job = self.after(1000, self.decrement_time)  # in milliseconds

        # timer reached 0 -> switching to next setting
        elif self.timer_running and current_time == "00:00":
            self.controller.timer_schedule.rotate(-1)  # takes the first value and places it at the end
            next_up = self.controller.timer_schedule[0]  # getting new state
            self.current_timer_label.set(next_up)  # set timer description label

            # set settings according to the current state:
            if next_up == "Pomodoro":
                pomodoro_time = int(self.controller.pomodoro.get())
                self.current_time.set(f"{self.controller.pomodoro.get():02d}:00")
            elif next_up == "Short Break":
                short_break_time = int(self.controller.short_break.get())
                self.current_time.set(f"{short_break_time:02d}:00")
            elif next_up == "Long Break":
                long_break_time = int(self.controller.long_break.get())
                self.current_time.set(f"{long_break_time:02d}:00")

            # iterate func using Frame.after
            self._timer_decrement_job = self.after(1000, self.decrement_time)


#app = PomodoroTimer()
#app.mainloop()
