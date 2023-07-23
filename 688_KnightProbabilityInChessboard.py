from functools import cache

class Solution:
    def knightProbability(self, n, K, r, c) -> float:
        dir = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2)]
        dp = [[[0] * n for _ in range(n)] for _ in range(K+1)]

        dp[0][r][c] = 1
        for k in range(1, K+1):
            for i in range(n):
                for j in range(n):
                    for di, dj in dir:
                        preI = i - di
                        preJ = j - dj
                        if 0 <= preI < n and 0 <= preJ < n:
                            dp[k][i][j] += (dp[k-1][preI][preJ]) / 8

        # print(dp)
        total = 0
        for i in range(n):
            for j in range(n):
                total += dp[K][i][j]
        return total
    
    def knightProbability(self, n, K, r, c) -> float:
        dir = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2)]
        curDP = [[0] * n for _ in range(n)]
        preDP = [[0] * n for _ in range(n)]

        preDP[r][c] = 1

        for k in range(1, K+1):
            for i in range(n):
                for j in range(n):
                    curDP[i][j] = 0
                    for di, dj in dir:
                        preI = i - di
                        preJ = j - dj
                        if 0 <= preI < n and 0 <= preJ < n:
                            curDP[i][j] += (preDP[preI][preJ]) / 8
            
            preDP, curDP = curDP, preDP

        # print(dp)
        total = 0
        for i in range(n):
            for j in range(n):
                total += preDP[i][j]
        return total
    
    def knightProbability(self, N, K, r, c) -> float:
        dir = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2)]

        @cache
        def dp(move, i, j):
            if move == 0:
                if i == r and j == c:
                    return 1
                else:
                    return 0
            
            proba = 0
            for di, dj in dir:
                preI = i - di
                preJ = j - dj
                if 0 <= preI < N and 0 <= preJ < N:
                    proba += dp(move-1, preI, preJ)

            proba /= 8
            return proba
        
        
        total = 0.0
        for i in range(N):
            for j in range(N):
                total += dp(K, i, j)

        return total
    

print(Solution().knightProbability(3,2,0,0))