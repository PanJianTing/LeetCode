class SnakeGame:

    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.COL = width
        self.ROW = height
        self.idx = 0
        self.cur_r = 0
        self.cur_c = 0
        self.food = food
        self.moves = [[0,0]]

    def move(self, direction: str) -> int:
        if direction == 'R':
            self.cur_c += 1
        elif direction == 'L':
            self.cur_c -= 1
        elif direction == 'U':
            self.cur_r -= 1
        else:
            self.cur_r += 1

        check_move = 0
        while check_move <= self.idx:
            check_idx = len(self.moves) - 1 - check_move
            if self.moves[check_idx] == [self.cur_r, self.cur_c]:
                return -1
            check_move += 1

        
        if 0 <= self.cur_r < self.ROW and 0 <= self.cur_c < self.COL:
            if self.idx < len(self.food) and self.food[self.idx] == [self.cur_r, self.cur_c]:
                self.idx += 1
            self.moves.append([self.cur_r, self.cur_c])
            return self.idx
        return -1


[["R"],["D"],["R"],["U"],["L"],["U"]]
sg = SnakeGame(3, 2, [[1,2],[0,1]])
print(sg.move('R'))
print(sg.move('D'))
print(sg.move('R'))
print(sg.move('U'))
print(sg.move('L'))
print(sg.move('U'))



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)