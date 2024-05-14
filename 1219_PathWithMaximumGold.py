from collections import deque

class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        
        
        def find_max_mine(i, j, visit):
            if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] == 0 or (i, j) in visit:
                return 0
            
            res = grid[i][j]
            visit.add((i, j))
            for di, dj in dirs:
                next_i = i + di
                next_j = j + dj

                res = max(res, grid[i][j] + find_max_mine(next_i, next_j, visit))
            visit.remove((i, j))
                
            return res
            
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 0:
                    res = max(res, find_max_mine(i, j, set()))
        return res
    
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        res = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j): 
            if i < 0 or j < 0 or i >= M or j >= N or grid[i][j] == 0:
                return 0
            
            origin = grid[i][j]
            res = grid[i][j]
            grid[i][j] = 0
            for di, dj in dirs:
                
                res = max(res, origin + dfs(i + di, j + dj))
            
            grid[i][j] = origin
            return res

        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i, j))
        return res
    
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        res = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(i, j):
            max_gold = grid[i][j]
            
            q = deque()
            q.append((i, j, grid[i][j], set([(i, j)])))

            while q:
                cur_i, cur_j, cur_gold, cur_visit = q.popleft()

                max_gold = max(max_gold, cur_gold)

                for di, dj in dirs:
                    next_i = cur_i + di
                    next_j = cur_j + dj

                    if 0 <= next_i < M and 0 <= next_j < N and grid[next_i][next_j] != 0 and (next_i, next_j) not in cur_visit:
                        cur_visit.add((next_i, next_j))
                        q.append((next_i, next_j, cur_gold + grid[next_i][next_j], set(cur_visit)))
                        cur_visit.remove((next_i, next_j))
            return max_gold
        
        for i in range(M):
            for j in range(N):
               res = max(res, bfs(i, j))

        return res
            

                    



    
print(Solution().getMaximumGold([[0, 6, 0],[5, 8, 7],[0, 9, 0]]))
print(Solution().getMaximumGold([[0, 0, 2],[13, 20, 36],[0 , 31, 27]]))
print(Solution().getMaximumGold([[1, 5, 0],[7, 2, 4]]))