import tkinter as tk
from tkinter import ttk
import requests
from section9_chat_app.frames.message_window import MessageWindow

messages = [{"message": "Hello, world", "date": 15498487}]
message_labels = []


class Chat(ttk.Frame):
    def __init__(self, container, background, **kwargs):
        super().__init__(container, **kwargs)

        # grid config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #       --messages section--

        # messages window:
        self.message_window = MessageWindow(self, background=background)
        self.message_window.grid(row=0, column=0, sticky="NSEW", pady=5)

        #       --fetch and post messages--

        # input frame:
        input_frame = ttk.Frame(self, padding=10, style="Controls.TFrame")
        input_frame.grid(row=1, column=0, sticky="EW")

        # input text box:
        self.message_input = tk.Text(input_frame, height=3)
        self.message_input.pack(expand=True, fill="both", side="left", padx=(0, 10))

        # post button:
        message_submit = ttk.Button(
            input_frame,
            text="Send",
            style="SendButton.TButton",
            command=self.post_message
        )
        message_submit.pack()

        # fetch button:
        message_fetch = ttk.Button(
            input_frame,
            text="fetch",
            style="FetchButton.TButton",
            command=self.get_messages
        )
        message_fetch.pack()  # since we pack this widget, all other widgets in the input_frame must use pack as well

        self.message_window.update_message_widgets(messages, message_labels)

    # post a message and send it to the api
    def post_message(self):
        body = self.message_input.get("1.0", "end").strip()  # get input from text box
        requests.post("http://167.99.63.70/message", json={"message": body})  # a post request to the api
        self.message_input.delete("1.0", "end")  # delete the posted message
        self.get_messages()  # refreshes the messages and show the added message

        # makes an api request for new messages and calls update_message_widgets
    def get_messages(self):
        global messages  # creating a global messages variable
        messages = requests.get("http://167.99.63.70/messages").json()  # making an api request
        self.message_window.update_message_widgets(messages, message_labels)  # create new labels for each new message
        self.after(150, lambda: self.message_window.yview_moveto(1.0))  # scroll to the last message after 150 millisecond

