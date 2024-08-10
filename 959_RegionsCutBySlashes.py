from collections import deque

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        N = len(grid)
        expand_grid = [[0] * (N*3) for _ in range(N*3)]
        ans = 0

        for i in range(N):
            for j in range(N):
                cur_i = i * 3
                cur_j = j * 3
                if grid[i][j] == '/':
                    expand_grid[cur_i][cur_j + 2] = 1
                    expand_grid[cur_i + 1][cur_j + 1] = 1
                    expand_grid[cur_i + 2][cur_j] = 1
                
                if grid[i][j] == '\\':
                    expand_grid[cur_i][cur_j] = 1
                    expand_grid[cur_i + 1][cur_j + 1] = 1
                    expand_grid[cur_i + 2][cur_j + 2] = 1
        
        
        for i in range(len(expand_grid)):
            for j in range(len(expand_grid)):

                if expand_grid[i][j] == 0:
                    expand_grid[i][j] = 1
                    q = deque()
                    q.append((i, j))

                    while q:
                        cur_i, cur_j = q.popleft()
                        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            next_i = cur_i + di
                            next_j = cur_j + dj

                            if 0 <= next_i < len(expand_grid) and 0 <= next_j < len(expand_grid) and expand_grid[next_i][next_j] == 0:
                                expand_grid[next_i][next_j] = 1
                                q.append((next_i, next_j))
                    ans += 1

        return ans
    
print(Solution().regionsBySlashes([" /","/ "]))