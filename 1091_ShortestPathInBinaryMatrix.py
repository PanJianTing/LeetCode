from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        n = len(grid)
        goal = (n-1, n-1)

        dir = ((-1,-1), (-1, 0), (-1 , 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        visited = set()
        
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        q = deque()
        q.append((0, 0, 1))

        while q:
            i, j, path = q.popleft()
            # grid[i][j] = 1
            visited.add((i,j))
            
            if  goal == (i, j):
                return path
            
            for dx, dy in dir:
                nI = i + dx
                nJ = j + dy

                if 0 <= nI < n and 0 <= nJ < n and grid[nI][nJ] == 0 and (nI, nJ) not in visited:
                    # grid[nI][nJ] = 1
                    visited.add((nI, nJ))
                    q.append((nI, nJ, path + 1))
            
        return -1
    
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        n = len(grid)
        goal = (n-1, n-1)

        dir = ((-1,-1), (-1, 0), (-1 , 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        # visited = set()
        
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        q = deque()
        q.append((0, 0, 1))

        while q:
            i, j, path = q.popleft()
            grid[i][j] = 1
            # visited.add((i,j))
            
            if  goal == (i, j):
                return path
            
            for dx, dy in dir:
                nI = i + dx
                nJ = j + dy

                if 0 <= nI < n and 0 <= nJ < n and grid[nI][nJ] == 0:
                    grid[nI][nJ] = 1
                    # visited.add((nI, nJ))
                    q.append((nI, nJ, path + 1))
            
        return -1
    
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = [(0, 0, 1)]
        grid[0][0] = 1
        for i, j, d in q:
            if i == n-1 and j == n-1: return d
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    q.append((x, y, d+1))
        
        return -1
    
print(Solution().shortestPathBinaryMatrix([[0,1], [1,0]]))
print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(Solution().shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,1]]))




