import mouse
#import time
from time import sleep
import threading

https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/

#from tkinter import *
import tkinter
#from tkinter import ttk

isStarted = 0
myText="START"
my_x=50
my_y=120
x=0
y=0

def change_button_text():
    global isStarted
    global button
    global t1
    print("Enter change_button_text")
    print("Number of thread: ",  t1.ac)
    if(button.cget('text') == "START"):
        button.config(text="STOP")
        isStarted = 1
        print(" Mode Start")
    elif(button.cget('text') == "STOP"):
        button.config(text="START")
        isStarted = 0
        t1.stop()
    else: print("Text de button inconnu")
    print("Exit change_button_text")


#Algo de move mouse
def keep_alive_session():
    global isStarted
    global button
    print("Enter keep_alive_session")
    if(not isStarted): 
        change_button_text()
        mouse.move(12,36,1,1)
    while (isStarted == 1):
        print(mouse.get_position())
        (x,y)=mouse.get_position()
        mouse.move(x,y+2,1,1)
        time.sleep(3)

    print("Exit keep_alive_session")


def my_thread():
    global t1
	# Call work function
    t1=threading.Thread(target=keep_alive_session)
    t1.start()



gui = tkinter.Tk()
gui.geometry("120x50+0+0")
button = tkinter.Button(
    gui,
    text=myText,
    command=my_thread
)
button.place(bordermode="inside" ,height=my_x, width=my_y)

gui.mainloop()
exit(0)
