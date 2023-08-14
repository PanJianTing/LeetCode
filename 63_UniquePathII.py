class Solution:
    def uniquePathsWithObstacles(self, grid) -> int:
        M = len(grid)
        N = len(grid[0])

        dp = [[0] * N for _ in range(M)]

        if grid[0][0]:
            return 0
        else:
            dp[0][0] = 1

        for i in range(1, N):
            if grid[0][i] == 0:
                dp[0][i] = dp[0][i-1]

        for j in range(1, M):
            if grid[j][0] == 0:
                dp[j][0] = dp[j-1][0]


        for i in range(1, M):
            for j in range(1, N):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[M-1][N-1]
    
    def uniquePathsWithObstacles(self, grid) -> int:
        N = len(grid[0])
        dp = [0] * N

        if grid[0][0]:
            return 0
        else:
            dp[0] = 1

        for i in range(1, N):
            if grid[0][i] == 0:
                dp[i] = dp[i-1]
        
        for i in range(1, len(grid)):
            if grid[i][0]:
                dp[0] = 0
            for j in range(1, N):
                if grid[i][j]:
                    dp[j] = 0
                else:
                    dp[j] += dp[j-1]

        return dp[N-1]


print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(Solution().uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]]))
print(Solution().uniquePathsWithObstacles([[0,1],[0,0]]))
print(Solution().uniquePathsWithObstacles([[0],[1]]))