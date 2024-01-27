from collections import deque
from collections import defaultdict
from functools import cache


class Solution:
    # BFS MLE
    def findPaths(self, m, n, maxMove, startRow, startColumn) -> int:

        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        q = deque()
        q.append((startRow, startColumn))

        while q and maxMove > 0:
            curNode = len(q)
            
            for _ in range(curNode):
                curR, curC = q.popleft()
                res = 0
                for dr, dc in dirs:
                    nextR = curR + dr
                    nextC = curC + dc
                    if 0 <= nextR < m and 0 <= nextC < n:
                        q.append((nextR, nextC))
                            
                    else:
                        res += 1
                ans += res
            maxMove -= 1
        return ans
    
    def findPaths(self, m, n, maxMove, startRow, startColumn) -> int:

        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(curR, curC, move) -> int:
            if 0 <= curR < m and 0 <= curC < n:
                if move > 0:
                    res = 0
                    for dr, dc in dirs:
                        res += dp(curR + dr, curC + dc, move - 1)
            
                    return res
                else:
                    return 0
            else:
                return 1
        
        return dp(startRow, startColumn, maxMove) % MOD
    
    # TLE
    def findPaths(self, m, n, maxMove, r, c) -> int:
        
        if r < 0 or r >= m or c < 0 or c >= n:
            return 1
        if maxMove == 0:
            return 0
        
        MOD = 10 ** 9 + 7
        dir1 = self.findPaths(m, n, maxMove-1, r-1, c)
        dir2 = self.findPaths(m, n, maxMove-1, r+1, c)
        dir3 = self.findPaths(m, n, maxMove-1, r, c-1)
        dir4 = self.findPaths(m, n, maxMove-1, r, c+1)
        
        return (dir1 + dir2 + dir3 + dir4) % MOD
    
    def findPaths(self, m, n, maxMove, startR, startC) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def recursion(r, c, move) -> int:
            if r < 0 or c < 0 or r >= m or c >= n:
                return 1
            if move == 0:
                return 0
            return recursion(r+1, c, move-1) + recursion(r-1, c, move-1) + recursion(r, c+1, move-1) + recursion(r, c-1, move-1)
        
        return recursion(startR, startC, maxMove) % MOD
    

    def findPaths(self, m, n, maxMove, startR, startC) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        dp = [[0] * n for _ in range(m)]

        dp[startR][startC] = 1

        for _ in range(maxMove):
            temp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        res += dp[i][j]
                    if j == n - 1:
                        res += dp[i][j]
                    if i == 0:
                        res += dp[i][j]
                    if j == 0:
                        res += dp[i][j]
                    
                    if i-1 >= 0:
                        temp[i][j] += dp[i-1][j]
                    if i+1 < m:
                        temp[i][j] += dp[i+1][j]
                    if j-1 >= 0:
                        temp[i][j] += dp[i][j-1]
                    if j+1 < n:
                        temp[i][j] += dp[i][j+1]
            dp = temp
        return res % MOD

                
    
# print(Solution().findPaths(2,2,2,0,0))
print(Solution().findPaths(1,3,3,0,1))
         