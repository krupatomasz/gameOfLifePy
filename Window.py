from tkinter import *
from Board import *

class Window:
    def __init__(self):
        self.master = Tk()

        self.pixels = 10

        canvas = Canvas(self.master, width=500, height=500)
        self.board = Board(canvas, self.pixels, True)
        self.board.draw()

        menu = self.getMenuPanel()

        canvas.grid(column=0, row=0, rowspan = 50)
        menu.grid(column=1, row=0)

        self.pauseFlag = False

    def task(self):
        if not self.pauseFlag:
            self.board.next()
        self.master.after(1000, self.task)

    def mainloop(self):
        self.master.after(1000, self.task)
        self.master.mainloop()

    def getMenuPanel(self):
        menu = Frame()
        pauseButton = Button(menu, text="Pause/Run", command=self.pauseToggle)
        pauseButton.grid(row=0)

        patternCanvas = Canvas(menu, width=40, height=40)
        patternCanvas.grid(row=1)
        pattern = Board(patternCanvas, self.pixels, False)
        pattern.board[1][1] = True
        pattern.board[1][2] = True
        pattern.board[2][1] = True
        pattern.board[2][2] = True
        pattern.draw()

        return menu


    def pauseToggle(self):
        self.pauseFlag = not self.pauseFlag