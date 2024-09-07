import tkinter as tk
from tkinter import ttk
from time import sleep
#from threading import Thread
import threading
from queue import Queue


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
    

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("120x50+0+0")
        self.queue_message = Queue()
        self.create_frame_button().pack(expand=True)
#        self.bind("<<CheckQueue>>", self.check_queue)


    def create_frame_button(self) -> ttk.Frame:
        self.frame_buttons = ttk.Frame(self)
        self.style_start = ttk.Style()
        self.style_start.theme_use("clam")
        self.style_start.configure("Start.TButton", font=("Cooper Black", 20), foreground="white", background="green")
        self.style_stop = ttk.Style()
        self.style_stop.theme_use("clam")
        self.style_stop.configure("Stop.TButton", font=("Cooper Black", 20), foreground="black", background="red")
        self.start_button = ttk.Button(self.frame_buttons, 
                                        text = "START",
                                        style="Start.TButton",
                                        command= self.on_start_button_clicked)
        self.start_button.config()
        self.start_button.pack()
        return self.frame_buttons
    


    def on_start_button_clicked(self):
        print("Enter on_start_button_clicked")

        if StoppableThread.stopped:
            print("===>>Syntaxe error")
            #StoppableThread.stop()

        new_thread = StoppableThread(target=self.move_process, 
                    args=(), 
                    daemon=True)
        new_thread.start()
        print("Nbre de thread: ", new_thread)
        print("Exit  on_start_button_clicked")



    def move_process(self):
        print("Enter move_process")

        self.start_button.configure(style="Stop.TButton")
       # self.start_button.config(background="red")

        for progress in range(1, 11):
            print(progress)
            self.start_button.configure(text=f"STOP \n Progression:{progress}")
            sleep(1)
        print("Exit move_process")


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()