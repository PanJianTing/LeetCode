from functools import cache

class Solution:
    def maxScore(self, a: list[int], b: list[int]) -> int:
        M = len(a)
        N = len(b)

        @cache
        def dp(idx_a, idx_b):
            if idx_a == M:
                return 0
            if idx_b >= N:
                return float('-inf')
            
            take = a[idx_a] * b[idx_b] + dp(idx_a + 1, idx_b + 1)
            no_take = dp(idx_a, idx_b + 1)
            return max(take, no_take)

        return dp(0, 0)
    

    def maxScore(self, a: list[int], b: list[int]) -> int:
        N = len(b)

        dp = [[float('-inf')] * (N+1) for _ in range(5)]

        for j in range(N + 1):
            dp[0][j] = 0

        for idx_a in range(1, 5):
            for idx_b in range(1, N+1):
                take = dp[idx_a-1][idx_b-1] + a[idx_a-1] * b[idx_b-1]
                no_take = dp[idx_a][idx_b-1]
                dp[idx_a][idx_b] = max(take, no_take)

        return dp[4][N]
    
print(Solution().maxScore([3,2,5,6], [2,-6,4,-5,-3,2,-7]))
print(Solution().maxScore([-1,4,5,-2], [-5,-1,-3,-2,-4]))
print(Solution().maxScore([-7,5,-10,-10], [7,-8,-1,2,4,8,-5,-5,5,-2,4]))