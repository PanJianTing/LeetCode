from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        N = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValidCell(i, j):
            if 0 <= i < N and 0 <= j < N:
                return True
            return False
        
        def isValidSafeness(min_safeness):
            
            if grid[0][0] < min_safeness or grid[-1][-1] < min_safeness:
                return False
            
            q = deque()
            q.append((0, 0))
            visited = [[False] * N for _ in range(N)]
            visited[0][0] = True

            while q:
                cur_i, cur_j = q.popleft()
                if (cur_i == N-1) and (cur_j == N-1):
                    return True
                
                for di, dj in dirs:
                    next_i = cur_i + di
                    next_j = cur_j + dj

                    if isValidCell(next_i, next_j) and visited[next_i][next_j] == False and grid[next_i][next_j] >= min_safeness:
                        q.append((next_i, next_j))
                        visited[next_i][next_j] = True
            return False

        q = deque()
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q.append((i, j))
                else:
                    grid[i][j] = -1
        while q:
            size = len(q)
            while size > 0:
                cur_i, cur_j = q.popleft()
                val = grid[cur_i][cur_j]
                for di, dj in dirs:
                    next_i = cur_i + di
                    next_j = cur_j + dj

                    if isValidCell(next_i, next_j) and grid[next_i][next_j] == -1:
                        grid[next_i][next_j] = val + 1
                        q.append((next_i, next_j))
                size -= 1
        
        st = 0
        end = 0
        res = -1
        for i in range(N):
            for j in range(N):
                end = max(end, grid[i][j])

        while st <= end:
            mid = st + ((end - st) >> 1)

            if isValidSafeness(mid):
                res = mid
                st = mid + 1
            else:
                end = mid - 1
        return res
    

print(Solution().maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]))
print(Solution().maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]]))
print(Solution().maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))
    
