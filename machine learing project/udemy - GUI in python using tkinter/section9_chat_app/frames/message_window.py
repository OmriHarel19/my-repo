import tkinter as tk
from tkinter import ttk
import datetime
from PIL import Image, ImageTk

# defines:
MAX_MESSAGE_WIDTH = 800


class MessageWindow(tk.Canvas):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs, highlightthickness=0)  # remove a default border of canvas

        #       --properties--

        # message frame
        self.message_frame = ttk.Frame(self, style="Messages.TFrame")
        self.message_frame.columnconfigure(0, weight=1)

        # scrollable window
        # (0,0): position of the window on the canvas, anchor: the point on the window to be placed at (0,0)
        self.scrollable_window = self.create_window((0, 0), window=self.message_frame, anchor="nw")

        #       --event handlers--

        # handle resizing of the message frame
        def configure_scroll_region(event):
            # updating the canvas scroll region to all available space
            self.configure(scrollregion=self.bbox("all"))

        # handle resizing of the canvas
        def configure_window_size(event):
            # update scrollable window width to match the canvas width (to not create horizontal scrolling)
            self.itemconfig(self.scrollable_window,
                            width=self.winfo_width())  # update window width using canvas (and not tk)

        #       --event binding--

        # bind message frame "Configure" event (which is change in size) to configure_scroll_region
        self.message_frame.bind("<Configure>", configure_scroll_region)

        # bind canvas configure event to configure_window_size
        self.bind("<Configure>", configure_window_size)

        # bind canvas MouseWheel event to the mouse wheel scroll function:
        self.bind_all("<MouseWheel>", self._on_mousewheel)  # use bind_all because the scrollable window is the only scrollable widget in the app.

        # add scroll bar:
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        # connect scroll bar and canvas
        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)  # move the canvas to the bottom of the scrollable are - makes the content in the same place every time

    # enable scroll with mouse wheel method
    def _on_mousewheel(self, event):
        # for info:
        # https://stackoverflow.com/questions/17355902/tkinter-binding-mousewheel-to-scrollbar/17457843#17457843
        self.yview_scroll(-int(event.delta/120), "units")

    # runs over the messages list and adds all new messages in labels
    def update_message_widgets(self, messages, message_labels):

        # getting content of all existing labels
        existing_labels = [
            (message["text"], time["text"]) for message, time in message_labels
        ]

        # running on all messages:
        for message in messages:
            # creating a datetime obj and formatting to a readable str
            message_time = datetime.datetime.fromtimestamp(message["date"]).strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            # check if a message of same content and same time do not exist in data
            if (message["message"], message_time) not in existing_labels:
                self._create_message_container(message["message"], message_time, message_labels)

    #           --private helper methods for  update_message_widgets()--

    # creates a new container from for a message, then calls the _create_message_bubble method
    def _create_message_container(self, message_content, message_time, message_labels):

        # create a new message container frame
        container = ttk.Frame(self.message_frame, style="Messages.TFrame")
        container.columnconfigure(1, weight=1)
        container.grid(sticky="EW", padx=(10, 50), pady=10)

        # configure message labels width according to container width:
        def reconfigure_message_labels(event):
            for label, _ in message_labels:
                label.configure(wraplength=min((container.winfo_width() - 100), MAX_MESSAGE_WIDTH))

        # bind the container configure to reconfigure_message_labels
        container.bind("<Configure>", reconfigure_message_labels)

        self._create_message_bubble(container, message_content, message_time, message_labels)

    # creates a of (avatar img,time,message) labels, places them in the container and add them to message_labels
    def _create_message_bubble(self, container, message_content, message_time, message_labels):
        # open img:
        avatar_img = Image.open("./assets/male.png")
        avatar_img = avatar_img.resize((25, 25), Image.ANTIALIAS)
        avatar_photo = ImageTk.PhotoImage(avatar_img)  # create a tk compatible img

        # create avatar label:
        avatar_label = ttk.Label(
            container,
            image=avatar_photo,
            style="Avatar.TLabel"
        )
        # assigning the avatar_photo as a custom property of the label so
        # it wouldn't be collected by the garbage-collector
        avatar_label.image = avatar_photo
        avatar_label.grid(row=0, column=0, rowspan=2, sticky="NEW", padx=(0, 10), pady=(5, 0))

        # create a time label
        time_label = ttk.Label(
            container,
            text=message_time,
            style="Time.TLabel"
        )
        time_label.grid(row=0, column=1, sticky="NEW")

        # create a message label
        message_label = ttk.Label(
            container,
            text=message_content,  # each element in messages is a dictionary with a "message" key
            anchor="w",  # label is left aligned
            justify="center",  # texts is left aligned
            wraplength=800,
            style="Message.TLabel"
        )
        message_label.grid(row=1, column=1, sticky="NSEW")
        # add to data base
        message_labels.append((message_label, time_label))
