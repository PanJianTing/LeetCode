from functools import cache

class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dir = [(-1, 1), (0, 1), (1, 1)]
        ans = 0

        @cache
        def dfs(cur_r, cur_c):
            
            step = 0
            
            for dr, dc in dir:
                next_r = cur_r + dr
                next_c = cur_c + dc

                if 0 <= next_r < M and 0 <= next_c < N and grid[next_r][next_c] > grid[cur_r][cur_c]:
                    step = max(step, 1 + dfs(next_r, next_c))
            
            return step
        
        for i in range(M):
            ans = max(ans, dfs(i, 0))
        
        return ans
    
print(Solution().maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))
print(Solution().maxMoves([[3,2,4],[2,1,9],[1,1,7]]))


        