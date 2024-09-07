import mouse
import time
import tkinter
import threading

def start():
    while status:
        print("Hello")
        time.sleep(3)

def start_thread():
    t1= threading.Thread(target=start)
    status=True

def stop():
  status=False

gui = tkinter.Tk()
gui.geometry("120x50+0+0")
start_btn = tkinter.Button(gui,text="Start",command=start_thread)
start_btn.pack()
stop_btn = tkinter.Button(gui,text="Stop",command=start_thread)
stop_btn.pack()

gui.mainloop()
exit(0)