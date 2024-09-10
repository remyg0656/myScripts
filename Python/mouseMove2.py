import tkinter as tk
from tkinter import ttk
import threading
import time
from queue import Queue
import mouse
import datetime


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("120x50+0+0")
        self.queue_message = Queue()
        self.create_frame_button().pack(expand=True)
#       self.bind("<<CheckQueue>>", self.check_queue)
    
    def create_frame_button(self) -> ttk.Frame:
        self.frame_buttons = ttk.Frame(self)
        self.style_start = ttk.Style()
        self.style_start.theme_use("clam")
        self.style_start.configure("Start.TButton", font=("Cooper Black", 20), foreground="white", background="green")
        self.style_stop = ttk.Style()
        self.style_stop.theme_use("clam")
        self.style_stop.configure("Stop.TButton", font=("Cooper Black", 10), foreground="black", background="red")
        self.start_button = ttk.Button(self.frame_buttons, 
                                        style="Start.TButton",
                                        text="START", 
                                        command= self.on_start_button_clicked)
        self.start_button.pack()

        print("Exiting Main")
        return self.frame_buttons
    

    def move_process(self, id, stop):
        print("Enter move_process id", id, "Stop val: ", stop)
        progress=0
        while True:
            self.start_button.configure(style="Stop.TButton")
           # minute = progress
            self.start_button.configure(text=f"   STOP \nDepuis {progress}min")
            progress=progress+1

            hours, minutes, seconds, milliseconds = self.convert_elapsed_time(elapsed_time)
            print("Progress", progress, " <> ", mouse.get_position())
            (x,y)=mouse.get_position()
            mouse.move(x,y+2,1,1)
            time.sleep(3)

            if stop():
                self.start_button.configure(style="Start.TButton")
                self.start_button.config(text="START")

                print("\tExiting loop.")
                break
        print("Exit move_process")


    def on_start_button_clicked(self):
        print("Enter on_start_button_clicked => val:", self.start_button.cget('text'))
        
        if(self.start_button.cget('text') == "START"):
            self.stop_threads = False
            self.myThread = threading.Thread(target=self.move_process,
                                    args=(0, lambda: self.stop_threads))
            self.myThread.start()
        else:
            print('===> time to stop the threads.',self.start_button.cget('text'))
            self.stop_threads = True
            self.myThread.join
        print("Exit  on_start_button_clicked")

    def convert_elapsed_time(seconds):
        time_delta = datetime.timedelta(seconds=seconds)
        hours = time_delta.seconds // 3600
        minutes = (time_delta.seconds % 3600) // 60
        seconds = (time_delta.seconds % 3600) % 60
        milliseconds = time_delta.microseconds // 1000
        return hours, minutes, seconds, milliseconds

if __name__ == '__main__':
    main_window = MainWindow()
    main_window.mainloop()