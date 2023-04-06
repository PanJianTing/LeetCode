from collections import deque

class Solution:
    def bfs(self, x: int, y: int, m: int, n: int, grid:list[list[int]], visited: set) -> bool:

        q = deque()
        dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        isClose = True
        q.append((x,y))
        visited.add((x, y))

        while len(q):
            x1,y1 = q.popleft()
            
            for i in range(4):
                dx,dy = dir[i]
                xx = x1 + dx
                yy = y1 + dy
                
                if xx < 0 or yy < 0 or yy >= m or xx >= n:
                    isClose = False
                elif grid[yy][xx] == 0 and (xx,yy) not in visited:
                    visited.add((xx, yy))
                    q.append((xx, yy))

        return isClose

    def dfs(self, x: int, y: int, m: int, n: int, grid: list[list[int]], visited: set) -> bool:

        if x < 0 or y < 0 or x >= n or y >= m:
            return False

        if grid[y][x] == 1 or (x, y) in visited:
            return True
        
        visited.add((x,y))
        
        dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        isClose = True

        for dx, dy in dir:
            xx = x + dx
            yy = y + dy

            if self.dfs(xx, yy, m, n, grid, visited) == False:
                isClose = False
            
        return isClose
    


    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0
        visited = set()

        for i in range(m):
            for j in range(n):
                # if grid[i][j] == 0 and (j, i) not in visited and self.bfs(j, i, m, n, grid, visited):
                #     ans += 1

                if grid[i][j] == 0 and (j, i) not in visited and self.dfs(j, i, m, n, grid, visited):
                    ans += 1
        return ans
    

class Solution:
    def fill(self, x: int, y: int, grid:list[list[int]]) -> int:
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == 1:
            return 0
        grid[y][x] = 1
        return (grid[y][x] == 1) + self.fill(x+1, y, grid) + self.fill(x, y+1, grid) + self.fill(x-1, y, grid) + self.fill(x, y-1, grid)
    
    def closedIsland(self, grid: list[list[int]]) -> int:
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i * j * (len(grid) - (i+1)) * (len(grid[i]) - (j+1)) == 0:
                    self.fill(j, i, grid)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if self.fill(j, i, grid) > 0:
                    ans += 1
        return ans


                    