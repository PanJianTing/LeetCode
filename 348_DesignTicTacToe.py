class TicTacToe:

    n = 0
    times = 0
    board = [[]]

    def __init__(self, n: int):
        self.n = n
        self.times = 0
        self.board = [[0] * n for _ in range(n)]
    
    def move(self, r, c, p) -> int:
        self.board[r][c] = p
        self.times += 1
        if self.times < self.n:
            return 0
        
        if self.checkHorizontal(r, p) or self.checkVertical(c, p) or self.checkDiagonal(p) or self.checkReversDiagonal(p):
            return p
        return 0

    def checkHorizontal(self, r, p) -> bool:

        for i in range(self.n):
            if (self.board[r][i] == p) == False:
                return False
        return True
    
    def checkVertical(self, c, p) -> bool:
        for i in range(self.n):
            if (self.board[i][c] == p) == False:
                return False
        return True
    
    def checkDiagonal(self, p) -> bool:

        for i in range(self.n):
            if (self.board[i][i] == p) == False:
                return False
        return True
    
    def checkReversDiagonal(self, p) -> bool:
        total = self.n - 1

        for i in range(self.n):
            j = total - i
            if (self.board[i][j] == p) == False:
                return False
        return True

