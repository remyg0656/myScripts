import tkinter as tk
from tkinter import ttk
import threading
import time
from queue import Queue
import mouse
from datetime import datetime
import sys

counter = 82800
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("120x60+0+0")
        self.queue_message = Queue()
        self.create_frame_button().pack(expand=True)
#       self.bind("<<CheckQueue>>", self.check_queue)
    
    def create_frame_button(self) -> ttk.Frame:
        self.frame_buttons = ttk.Frame(self)
        self.style_start = ttk.Style()
        self.style_start.theme_use("clam")
        self.style_start.configure("Start.TButton", font=("impact", 23), foreground="white", background="green")
        self.style_stop = ttk.Style()
        self.style_stop.theme_use("clam")
        self.style_stop.configure("Stop.TButton", font=("impact", 15), foreground="black", background="red")
        self.start_button = ttk.Button(self.frame_buttons, 
                                        style="Start.TButton",
                                        text="START", 
                                        command= self.on_start_button_clicked)
        self.start_button.pack()

        #print("Exiting Main")
        return self.frame_buttons
    

    def move_process(self, id, stop):
        #print("Enter move_process id", id, "Stop val: ", stop)
        global counter
        while True:
            counter = counter + 1
            tt = datetime.fromtimestamp(counter)
            now = tt.strftime("%H:%M:%S")          
            self.start_button.configure(style="Stop.TButton")
            self.start_button.configure(text=f"   STOP \n{now}")

            #print("Progress", counter, " <> ", mouse.get_position())
            if(not(counter % 180 )): # On bouge d'1 pixel vers la droite toute les 3mins
                #print("\tOn bouge", counter)
                #(x,y)=mouse.get_position()
                #mouse.move(x,y+1,1,0)
                mouse.move(1,0,0,0)

            time.sleep(1)

            if stop():
                self.start_button.configure(style="Start.TButton")
                self.start_button.config(text="START")
                #print("\tExiting loop.")
                break
        #print("Exit move_process")


    def on_start_button_clicked(self):
        #print("Enter on_start_button_clicked => val:", self.start_button.cget('text'))
        
        if(self.start_button.cget('text') == "START"):
            self.stop_threads = False
            self.myThread = threading.Thread(target=self.move_process,
                                    args=(0, lambda: self.stop_threads))
            self.myThread.start()
        else:
            #print('===> time to stop the threads.',self.start_button.cget('text'))
            self.stop_threads = True
            self.myThread.join
        #print("Exit  on_start_button_clicked")

    def on_closing():
        main_window.destroy()
        sys.exit(0)


if __name__ == '__main__':
    main_window = MainWindow()
    main_window.protocol("WM_DELETE_WINDOW", MainWindow.on_closing )
    main_window.mainloop()