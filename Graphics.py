class Graphics:
    def __init__(self, board, canvas, pixels):
        self.board = board
        self.canvas = canvas
        self.pixels = pixels

    def draw(self):
        self.drawBoard()

    def drawBoard(self):
        width = self.board.width
        height = self.board.height
        for i in range(width):
            x = self.pixels * i
            self.canvas.create_line(x, 0, x, 20, fill="gray70")

        for i in range(height):
            y = self.pixels * i
            self.canvas.create_line(0, y, width * self.pixels, y, fill="gray70")

        for i in range(width):
            for j in range(height):
                x = i * self.pixels
                y = j * self.pixels
                if self.board.board[i][j] == True:
                    self.canvas.create_rectangle(x, y, x + self.pixels, y + self.pixels, fill="red")
                else:
                    self.canvas.create_rectangle(x, y, x + self.pixels, y + self.pixels, fill=self.canvas['background'])