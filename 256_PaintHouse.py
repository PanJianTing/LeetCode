from functools import cache

class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        N = len(costs)
        ans = float('inf')
        
        @cache
        def dp(idx, colorIdx) -> int:
            if idx == N:
                return 0
            res = float('inf')
            for i in range(3):
                if i == colorIdx:
                    continue
                res = min(res, dp(idx+1, i))
            return costs[idx][colorIdx] + res
        
        for i in range(3):
            ans = min(ans, dp(0, i))
        
        return ans

    def minCost(self, costs: list[list[int]]) -> int:
        N = len(costs)
        dp = [[0] * 3 for _ in range(N+1)]

        for i in range(1, N+1):
            dp[i][0] = costs[i-1][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i-1][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i-1][2] + min(dp[i-1][0], dp[i-1][1])

        return min(dp[N])

    def minCost(self, costs: list[list[int]]) -> int:
        N = len(costs)
        dp = costs[0]

        for i in range(1, N):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]

        return min(dp)
    

print(Solution().minCost([[17,2,17],[16,16,5],[14,3,19]]))