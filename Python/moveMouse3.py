import mouse
import time
from time import sleep
import threading
import queue

#https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/

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
    print("Number of thread: ",  t1)
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


def my_move_the_mouse():
    print("Enter my_move_the_mouse")
    while(button.cget('text') == "STOP"):
        print("\tPosition: ",mouse.get_position())
        (x,y)=mouse.get_position()
        mouse.move(x,y+2,1,1)
        time.sleep(3)
    print("Exit my_move_the_mouse")
  



""" def my_start():
    print("Enter my_start")
    print("\tPosition: ",mouse.get_position())
    if(button.cget('text') == "START"):
        button.config(text="STOP")
        button.config(background="red")
        print("\t\tIn the START if")
        my_move_the_mouse()

    elif(button.cget('text') == "STOP"):
        button.config(text="START")
        button.config(background="green")
        print("\t\tIn the STOP if")
    print("Exit  my_start") """

def my_start():
    print("Enter my_start")
    print("\tPosition: ",mouse.get_position())
    while True:
        text = task_queue.get()
        print("\t In the while", text)
        if(button.cget('text') == "START"):
            button.config(text="STOP")
            button.config(background="red")
            print("\t\tIn the START if")
            my_move_the_mouse()

        elif(button.cget('text') == "STOP"):
            button.config(text="START")
            button.config(background="green")
            print("\t\tIn the STOP if")
    print("Exit  my_start") 

def threaded_task():
    print("Enter threaded_task")
    text = button.cget('text')
    task_queue.put(text)
    time.sleep(1)
    print("Exit  threaded_task", text)

gui = tkinter.Tk()
gui.geometry("120x50+0+0")
task_queue = queue.Queue()

button = tkinter.Button(
    gui,
    text="START",
    background="green",
    activebackground="red",
    command=my_start
)
button.place(bordermode="inside" ,height=my_x, width=my_y)
threading.Thread(target=my_start, daemon=True).start()
threading.Thread(target=threaded_task, daemon=True).start()
gui.mainloop()
exit(0)
