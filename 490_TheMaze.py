from collections import defaultdict
from collections import deque

class Solution:
    # bfs
    def hasPath(self, maze, start, des) -> bool:
        R = len(maze)
        C = len(maze[0])
        q = deque()
        q.append((start[0], start[1]))
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visit = set()
        visit.add((start[0], start[1]))

        while(q):
            curR, curC = q.popleft()

            if curR == des[0] and curC == des[1]:
                return True

            for dr, dc in dir:
                nextR = curR
                nextC = curC
                while True:
                    tempR = nextR + dr
                    tempC = nextC + dc
                    if 0 <= tempR < R and 0 <= tempC < C and maze[tempR][tempC] == 0:
                        nextR = tempR
                        nextC = tempC
                    else:
                        break
                
                if (nextR, nextC) not in visit:
                    q.append((nextR, nextC))
                    visit.add((nextR, nextC))

        return False
    
    # dfs
    def hasPath(self, maze, start, des) -> bool:
        R = len(maze)
        C = len(maze[0])
        visit = set()

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(r, c):
            if [r, c] == des:
                return True
            
            visit.add((r,c))
            
            for dr, dc in dir:
                nextR = r
                nextC = c

                while True:
                    tempR = nextR + dr
                    tempC = nextC + dc

                    if 0 <= tempR < R and 0 <= tempC < C and maze[tempR][tempC] == 0:
                        nextR, nextC = tempR, tempC
                    else:
                        break
                
                if (nextR, nextC) not in visit:
                    if dfs(nextR, nextC):
                        return True
            
            return False
        
        return dfs(start[0], start[1])
    
print(Solution().hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]))
print(Solution().hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [3,2]))