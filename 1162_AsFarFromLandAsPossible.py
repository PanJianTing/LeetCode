from collections import deque
from queue import Queue
class Solution:
    #BFS using deque(better than Queue), time: O(n^2), space: O(n^2)
    def maxDistance(self, grid: list[list[int]]) -> int:
        # up, down, left, right
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        landQ = deque(())
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                visited[i][j] = grid[i][j]
                if grid[i][j] == 1:
                    landQ.append((i,j))

        if len(landQ) == 0 or len(landQ) == len(grid[0]) * len(grid):
            return -1

        distance = -1
        while len(landQ) != 0:
            
            size = len(landQ)
            while size > 0:
                land = landQ.popleft()

                for d in direction:
                    x = land[0] + d[0]
                    y = land[1] + d[1]

                    if x >= 0 and y >= 0 and x < len(grid) and y < len(grid) and visited[x][y] == 0:
                        visited[x][y] = 1
                        landQ.append((x,y))

                size -= 1
            distance += 1
        return distance

    #BFS using Queue(worst than deque), time: O(n^2), space: O(n^2)
    def maxDistance(self, grid: list[list[int]]) -> int:
        # up, down, left, right
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        landQ = Queue()
    
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                visited[i][j] = grid[i][j]
                if grid[i][j] == 1:
                    landQ.put((i,j))
       
        distance = -1
        while landQ.empty() == False:
            
            size = landQ.qsize()
            while size > 0:
                land = landQ.get()
                # print(land)

                for d in direction:
                    x = land[0] + d[0]
                    y = land[1] + d[1]
                    # print(x,y)

                    if x >= 0 and y >= 0 and x < len(grid) and y < len(grid) and visited[x][y] == 0:
                        visited[x][y] = 1
                        landQ.put((x,y))

                size -= 1
            distance += 1

        if distance == 0:
            return -1
        return distance

    
    #dp time: O(n^2), space: O(n^2)
    def maxDistance(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        MAX_DISTANCE = row + col + 1

        dist = [[MAX_DISTANCE] * col for _ in range(0, row)]
        
        # topleft to bottomright
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                else:
                    leftDist = MAX_DISTANCE
                    topDist = MAX_DISTANCE
                    if i > 0:
                        topDist = dist[i-1][j] + 1
                    if j > 0:
                        leftDist = dist[i][j-1] + 1

                    dist[i][j] = min(dist[i][j], min(topDist, leftDist))

        ans = -1

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                rightDist = MAX_DISTANCE
                bottomDist = MAX_DISTANCE

                if i < row-1:
                    bottomDist = dist[i+1][j] + 1
                    
                if j < col-1:
                    rightDist = dist[i][j+1] + 1

                dist[i][j] = min(dist[i][j], min(bottomDist, rightDist))

                ans = max(ans, dist[i][j])
        # print(ans)

        if ans == 0 or ans == MAX_DISTANCE:
            return -1
        return ans

    #dp time: O(n^2), space: O(1)
    def maxDistance(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        MAX_DISTANCE = row + col + 1

        
        # top-left to bottom-right
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = MAX_DISTANCE
                    leftDist = MAX_DISTANCE
                    topDist = MAX_DISTANCE
                    if i > 0:
                        topDist = grid[i-1][j] + 1
                    if j > 0:
                        leftDist = grid[i][j-1] + 1

                    grid[i][j] = min(grid[i][j], min(topDist, leftDist))

        ans = -1
        
        # bottom-right to top-left
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                rightDist = MAX_DISTANCE
                bottomDist = MAX_DISTANCE

                if i < row-1:
                    bottomDist = grid[i+1][j] + 1
                    
                if j < col-1:
                    rightDist = grid[i][j+1] + 1

                grid[i][j] = min(grid[i][j], min(bottomDist, rightDist))

                ans = max(ans, grid[i][j])
        # print(ans)

        if ans == 0 or ans == MAX_DISTANCE:
            return -1
        return ans


                

Solution().maxDistance([[1,0,1], [0,0,0], [1,0,1]])
Solution().maxDistance([[1,0,0], [0,0,0], [0,0,1]])