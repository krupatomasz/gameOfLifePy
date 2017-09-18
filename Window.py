from tkinter import *
from Board import *

class Window:
    def __init__(self):
        self.master = Tk()

        canvas = Canvas(self.master, width=500, height=500)
        canvas.pack()
        self.board = Board(canvas, 10)
        self.board.draw()

        menu = self.getMenuPanel()
        menu.pack()

        self.pauseFlag = False

    def task(self):
        if not self.pauseFlag:
            self.board.next()
        self.master.after(1000, self.task)

    def mainloop(self):
        self.master.after(1000, self.task)
        self.master.mainloop()

    def getMenuPanel(self):
        menu = Frame(height=100)
        pauseButton = Button(menu, text="Pause/Run", command=self.pauseToggle)
        pauseButton.pack()
        return menu


    def pauseToggle(self):
        self.pauseFlag = not self.pauseFlag