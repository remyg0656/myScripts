import tkinter as tk
from tkinter import ttk
from time import sleep
from threading import Thread
from queue import Queue
from enum import Enum, auto


class TicketPurpose(Enum):
    UPDATE_PROGRESS_TEXT = auto()

class Ticket:
    def __init__(self,
                 ticket_type: TicketPurpose,
                 ticket_value: str):
        self.ticket_type = ticket_type
        self.ticket_value = ticket_value


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.queue_message = Queue()
        self.create_frame_button().pack(expand=True)
        self.bind("<<CheckQueue>>", self.check_queue)



    def check_queue(self, event):
        """
            Read the queue
        """
        msg: Ticket
        msg =  self.queue_message.get()
        if msg.ticket_type == TicketPurpose.UPDATE_PROGRESS_TEXT:
            self.lbl_status.configure(text=msg.ticket_value)



    def create_frame_button(self) -> ttk.Frame:
        self.frame_buttons = ttk.Frame(self)
        self.btn_download = ttk.Button(self.frame_buttons, 
                                       text = "Download",
                                       command= self.on_download_button_clicked)
        self.btn_test = ttk.Button(self.frame_buttons, 
                                   text="Test",
                                   command=self.on_test_button_clicked)
        self.lbl_status = ttk.Label(self.frame_buttons)
        self.btn_download.pack()
        self.btn_test.pack()
        self.lbl_status.pack()

        return self.frame_buttons
    
    def on_download_button_clicked(self):
        new_thread = Thread(target=self.download, 
                            args=("sky.png", ), 
                            daemon=True)
        new_thread.start()

    def on_test_button_clicked(self):
        print("Test")


    
    def download(self, file_name: str):
        for progress in range(1, 11):
            print(progress)
            #self.lbl_status.configure(text=f"{progress}%")
            ticket = Ticket(ticket_type=TicketPurpose.UPDATE_PROGRESS_TEXT,
                            ticket_value=f"Downloading {file_name} ... {progress}%")
            self.queue_message.put(ticket)
            self.event_generate("<<CheckQueue>>")
            sleep(1)
        
        ticket= Ticket(ticket_type=TicketPurpose.UPDATE_PROGRESS_TEXT, ticket_value="Finished Downloading!")
        self.queue_message.put(ticket)
        self.event_generate("<<CheckQueue>>")

        


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
