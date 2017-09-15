from tkinter import *
from Board import *
import time
master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()

board = Board(w, 10)
board.draw()


def task():
    board.next()
    master.after(1000, task)


master.after(1000, task)
master.mainloop()