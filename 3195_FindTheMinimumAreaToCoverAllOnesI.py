class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        minR = M
        minC = N
        maxR = 0
        maxC = 0

        for r in range(M):
            for c in range(N):
                if grid[r][c]:
                    minR = min(minR, r)
                    minC = min(minC, c)
                    maxR = max(maxR, r)
                    maxC = max(maxC, c)
        

        return (maxR - minR + 1) * (maxC - minC + 1)
    
print(Solution().minimumArea([[0,1,0],[1,0,1]]))
print(Solution().minimumArea([[0,0],[1,0]]))