import copy

class Board:
    def __init__(self, canvas, pixels):
        self.canvas = canvas
        self.width = int(self.canvas['width']) // pixels
        self.height = int(self.canvas['height']) // pixels
        self.pixels = pixels
        self.board = []
        self.initBoard(self.board)

    def initBoard(self, board):
        for i in range(self.width):
            board.append([])
            for j in range(self.height):
                board[i].append(False)
        board[3][3] = True
        board[4][3] = True
        board[5][3] = True

    def draw(self):
        for i in range(self.width):
            x = 10*i
            self.canvas.create_line(x, 0, x, 20, fill="gray70")

        for i in range(self.height):
            y = 10*i
            self.canvas.create_line(0, y, self.width*self.pixels, y, fill="gray70")

        for i in range(self.width):
            for j in range(self.height):
                x = i * self.pixels
                y = j * self.pixels
                if self.board[i][j] == True:
                    self.canvas.create_rectangle(x, y, x+self.pixels, y+self.pixels, fill="red")
                else:
                    self.canvas.create_rectangle(x, y, x + self.pixels, y + self.pixels, fill=self.canvas['background'])


    def next(self):
        tmp = copy.deepcopy(self.board)

        for i in range(self.width):
            for j in range(self.height):
                cell = self.board[i][j]
                neighborsNo = self.getNeighboursNo(i, j)
                if cell == False:
                    if neighborsNo == 3:
                        tmp[i][j] = True
                else:
                    if neighborsNo != 2 and neighborsNo != 3:
                        tmp[i][j] = False
        self.board = tmp
        self.draw()


    def getNeighboursNo(self, x, y):
        res = 0
        if y==3:
        for i in range(x-1, x+2):
            for j in range(y-1,y+2):
                if (x == i and y == j) or not self.checkCoords(i, j):
                    continue
                else:
                    if self.board[i][j] == True:
                        res = res + 1
        return res

    def checkCoords(self, i, j):
        if i < 0 or j < 0:
            return False
        if i >= self.width or j >= self.height:
            return False
        return True