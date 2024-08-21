from functools import cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        N = len(piles)
        suffix = list(piles)

        for i in range(N-2, -1, -1):
            suffix[i] += suffix[i+1]

        @cache
        def dp(cur, max_idx):
            if cur + 2 * max_idx >= N:
                return suffix[cur]
            
            res = float('inf')
            for i in range(1, 2 * max_idx+1):
                res = min(res, dp(cur+i, max(max_idx, i)))
            
            return suffix[cur] - res

        return dp(0, 1)
    
    def stoneGameII(self, piles: list[int]) -> int:
        N = len(piles)
        dp = [[0] * (N+1) for _ in range(N+1)]

        suffix = [0] * (N+1)

        for i in range(N-1, -1, -1):
            suffix[i] += suffix[i+1] + piles[i]

        for i in range(N+1):
            dp[i][N] = suffix[i]
        
        for i in range(N-1, -1, -1):
            for j in range(N-1, 0, -1):
                for k in range(1, min(j << 1, N - i) + 1):
                    dp[i][j] = max(dp[i][j], suffix[i] - dp[i + k][max(j, k)])

        return dp[0][1]
    
print(Solution().stoneGameII([2,7,9,4,4]))
print(Solution().stoneGameII([1,2,3,4,5,100]))