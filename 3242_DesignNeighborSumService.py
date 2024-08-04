from collections import defaultdict
import heapq

class neighborSum:
    def __init__(self, grid: list[list[int]]):
        self.M = len(grid)
        self.N = len(grid[0])
        self.position_map = defaultdict(list)
        self.grid = grid

        for i in range(self.M):
            for j in range(self.N):
                self.position_map[grid[i][j]].append(i)
                self.position_map[grid[i][j]].append(j)

    def adjacentSum(self, value: int) -> int:
        cur_i, cur_j = self.position_map[value]
        res = 0

        if 0 <= cur_i - 1 < self.M:
            res += self.grid[cur_i-1][cur_j]
        
        if 0 <= cur_j - 1 < self.N:
            res += self.grid[cur_i][cur_j-1]
        
        if 0 <= cur_i + 1 < self.M:
            res += self.grid[cur_i+1][cur_j]

        if 0 <= cur_j + 1 < self.N:
            res += self.grid[cur_i][cur_j+1]

        return res

    def diagonalSum(self, value: int) -> int:
        cur_i, cur_j = self.position_map[value]
        res = 0

        if 0 <= cur_i - 1 < self.M and 0 <= cur_j - 1 < self.N:
            res += self.grid[cur_i-1][cur_j-1]

        if 0 <= cur_i - 1 < self.M and 0 <= cur_j + 1 < self.N:
            res += self.grid[cur_i-1][cur_j+1]

        if 0 <= cur_i + 1 < self.M and 0 <= cur_j - 1 < self.N:
            res += self.grid[cur_i+1][cur_j-1]

        if 0 <= cur_i + 1 < self.M and 0 <= cur_j + 1 < self.N:
            res += self.grid[cur_i+1][cur_j+1]
        
        return res
    

class neighborSum:
    def __init__(self, grid: list[list[int]]):
        self.N = len(grid)
        self.position_map = defaultdict(list)
        self.grid = grid

        for i in range(self.N):
            for j in range(self.N):
                self.position_map[grid[i][j]].append(i)
                self.position_map[grid[i][j]].append(j)

    def adjacentSum(self, value: int) -> int:
        cur_i, cur_j = self.position_map[value]
        res = 0

        dir = [(cur_i-1, cur_j), (cur_i, cur_j-1), (cur_i+1, cur_j), (cur_i, cur_j+1)]

        for i,j in dir:
            if 0 <= i < self.N and 0 <= j < self.N:
                res += self.grid[i][j]

        return res

    def diagonalSum(self, value: int) -> int:
        cur_i, cur_j = self.position_map[value]
        res = 0
        dir = [(cur_i-1, cur_j-1), (cur_i-1, cur_j+1), (cur_i+1, cur_j-1), (cur_i+1, cur_j+1)]

        for i,j in dir:
            if 0 <= i < self.N and 0 <= j < self.N:
                res += self.grid[i][j]
        
        return res
    