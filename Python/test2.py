import tkinter as tk
import threading
import queue
import time

def update_label():
    print("Enter update_label")
    while True:
        text = task_queue.get()
        print("\t In the while", text)
        label.config(text=text)
        task_queue.task_done()

    print("Exit update_label")


def threaded_task():
    print("Enter threaded_task")
    for i in range(10):
        print("\t In the IF", i)
        task_queue.put(f"Task {i} completed")
        time.sleep(1)
    print("Exit  threaded_task")


root = tk.Tk()

task_queue = queue.Queue()

label = tk.Label(root, text="Waiting for tasks...")
label.pack()

threading.Thread(target=update_label, daemon=True).start()
threading.Thread(target=threaded_task, daemon=True).start()

root.mainloop()