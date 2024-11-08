import threading
import time
import queue
import sys
from tkinter import *


ws = Tk()

ws.geometry("200x200")

comque= queue.Queue()

def my_exit():
    print("Enter my_exit")
    for curThread in threading.enumerate():
        print(curThread.name)
    sys.exit()


def timeThread():
    print("Enter timeThread")
    prestime = 0
    while 1:      
        comque.put(prestime)        
        try:
            ws.event_generate('<<Trululu>>', when='tail')
        
        except TclError:
            my_exit()
            break
   
        time.sleep(1)
        prestime += 1
        print("prestime:", prestime)

    print("Exit timeThread")

clcvar = IntVar()
Label(ws, textvariable=clcvar, width=9).pack(pady=10)
Button(ws, text="quit", command=my_exit).pack(pady=20)


def timeChanged(event):
    print("Enter timeChanged")
    clcvar.set(comque.get())
    print("Exit timeChanged")

ws.bind('<<Trululu>>', timeChanged)


Thr=threading.Thread(target=timeThread)
Thr.start()

ws.mainloop()