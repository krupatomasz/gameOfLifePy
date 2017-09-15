class Board:
    def __init__(self, canvas, pixels):
        self.canvas = canvas
        self.width = int(self.canvas['width']) // pixels
        self.height = int(self.canvas['height']) // pixels
        self.pixels = pixels
        self.board = []
        self.initBoard(self.board)

    def initBoard(self, board):
        for i in range(self.height):
            board.append([])
            for j in range(self.width):
                board[i].append(False)
        board[3][3] = True
        board[4][3] = True
        board[5][3] = True

    def draw(self):
        for i in range(self.width):
            y = 10*i
            self.canvas.create_line(y, 0, y, self.height*self.pixels, fill="gray70")

        for i in range(self.height):
            y = 10*i
            self.canvas.create_line(0, y, self.width*self.pixels, y, fill="gray70")

        for i in range(self.height):
            for j in range(self.width):
                x = i * self.pixels
                y = j * self.pixels
                if self.board[i][j] == True:
                    self.canvas.create_rectangle(x, y, x+self.pixels, y+self.pixels, fill="red")
                else:
                    self.canvas.create_rectangle(x, y, x + self.pixels, y + self.pixels, fill=self.canvas['background'])

    def next(self):
        tmp = self.board.copy()

        for i in range(self.height):
            for j in range(self.width):
                cell = self.board[i][j]
                neighborsNo = self.getNeighboursNo(i, j)
                if(cell == False):
                    if(neighborsNo == 3):
                        tmp[i][j] = True
                else:
                    if neighborsNo != 2 and neighborsNo != 3:
                        tmp[i][j] = False
        self.board = tmp
        self.draw()


    def getNeighboursNo(self, x, y):
        res = 0
        for i in range(x-1, x+2):
            for j in range(y-1,y+2):
                if not self.checkCoords(i, j):
                    continue
                else:
                    if self.board[i][j] == True:
                        res = res + 1
        return res

    def checkCoords(self, i, j):
        if i < 0 or j < 0:
            return False
        if i >= self.height or j >= self.width:
            return False
        return True