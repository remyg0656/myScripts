import tkinter
import threading
import time



def __init__(self, master):
    self.master = master
    self.test_button = tkinter.Button(self.master, command=self.tb_click)
    self.test_button.configure(
        text="Start", background="Grey",
        padx=50
        )
    self.test_button.pack(side="TOP")

def progress(self):
    self.prog_bar = tkinter.Progressbar(
        self.master, orient="horizontal",
        length=200, mode="indeterminate"
        )
    self.prog_bar.pack(side="TOP")

def tb_click(self):
    self.progress()
    self.prog_bar.start()
    # Simulate long running process
    t = threading.Thread(target=time.sleep, args=(5,))
    t.start()
    t.join()
    self.prog_bar.stop()

gui = tkinter.Tk()
gui.title("Test Button")
gui.mainloop()