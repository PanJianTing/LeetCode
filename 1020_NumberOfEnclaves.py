from collections import deque

class Solution:
    def fill(self, x: int, y: int, grid: list[list[int]]) -> int:
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == 0:
            return 0
        grid[y][x] = 0
        return 1 + self.fill(x+1, y, grid) + self.fill(x-1, y, grid) + self.fill(x, y+1, grid) + self.fill(x, y-1, grid)


    def numEnclaves(self, grid: list[list[int]]) -> int:
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if i * j * (len(grid) - (i+1)) * (len(grid[i]) - (j+1)) == 0:
                    self.fill(j, i, grid)
        ans = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    ans += self.fill(j, i, grid)

        return ans


class Solution:

    def bfs(self, x: int, y: int, grid: list[list[int]], visited: set):

        q = deque()

        q.append((x,y))
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited.add((x,y))

        while len(q):
            curX, curY = q.popleft()
            grid[curY][curX] = 0
            for dx, dy in dir:
                nextX = curX + dx
                nextY = curY + dy

                if nextX < 0 or nextY < 0 or nextX >= len(grid[0]) or nextY >= len(grid):
                    continue
                elif grid[nextY][nextX] == 1 and (nextX, nextY) not in visited:
                    visited.add((nextX, nextY))
                    q.append((nextX, nextY))

        return


    def numEnclaves(self, grid: list[list[int]]) -> int:

        visited = set()
        ans = 0

        m = len(grid)
        n = len(grid[0])

        for i in range(0, n):
            if grid[0][i] == 1 and (i, 0) not in visited:
                self.bfs(i, 0, grid, visited)
            
            if grid[m-1][i] == 1 and (i, m-1) not in visited:
                self.bfs(i, m-1, grid, visited)

        for j in range(0, m):
            if grid[j][0] == 1 and (0, j) not in visited:
                self.bfs(0, j, grid, visited)

            if grid[j][n-1] == 1 and (n-1, j) not in visited:
                self.bfs(n-1, j, grid, visited)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 1:
                    ans += 1
        return ans
    

class Solution:
    def dfs(self, x: int, y: int, grid: list[list[int]]):

        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == 0:
            return
        grid[y][x] = 0
        self.dfs(x+1, y, grid)
        self.dfs(x-1, y, grid)
        self.dfs(x, y+1, grid)
        self.dfs(x, y-1, grid)

        return
    
    def numEnclaves(self, grid: list[list[int]]) -> int:

        visited = set()
        ans = 0

        m = len(grid)
        n = len(grid[0])

        for i in range(0, n):
            if grid[0][i] == 1 and (i, 0) not in visited:
                self.dfs(i, 0, grid)
            
            if grid[m-1][i] == 1 and (i, m-1) not in visited:
                self.dfs(i, m-1, grid)

        for j in range(0, m):
            if grid[j][0] == 1 and (0, j) not in visited:
                self.dfs(0, j, grid)

            if grid[j][n-1] == 1 and (n-1, j) not in visited:
                self.dfs(n-1, j, grid)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 1:
                    ans += 1
        return ans
    

class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:

        res = 0
        q = deque()

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                res += grid[i][j]
                if i * j * (len(grid) - (i+1)) * (len(grid[i]) - (j+1)) == 0:
                    q.append((i,j))

        while len(q):
            r, c = q.popleft()
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                continue
            grid[r][c] = 0
            res -= 1
            q.append((r+1, c))
            q.append((r-1, c))
            q.append((r, c+1))
            q.append((r, c-1))

        return res


        
        
                
