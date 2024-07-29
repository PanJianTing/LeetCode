from functools import cache

class Solution:
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        N = len(prob)
        
        @cache
        def dp(idx, cnt):
            
            if cnt > target:
                return 0
            
            if idx == N:
                if target == cnt:
                    return 1
                return 0

            return dp(idx+1, cnt+1) * prob[idx] + dp(idx+1, cnt) * (1-prob[idx])

        return dp(0, 0)
    
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        N = len(prob)
        dp = [[0.0] * (target+1) for _ in range(N+1)]
        dp[0][0] = 1.0

        for i in range(1, N+1):
            dp[i][0] = dp[i-1][0] * (1 - prob[i-1])
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j-1] * prob[i-1] + dp[i-1][j] * (1- prob[i-1])

        
        return dp[N][target]
    
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        N = len(prob)
        dp = [0.0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, N+1):
            for j in range(target, 0, -1):
                dp[j] = dp[j-1] * prob[i-1] + dp[j] * (1 - prob[i-1])
            dp[0] = dp[0] * (1-prob[i-1])

        return dp[target]
    


print(Solution().probabilityOfHeads([0.2,0.8,0,0.3,0.5], 3))
print(Solution().probabilityOfHeads([0.4], 1))
print(Solution().probabilityOfHeads([0.5,0.5,0.5,0.5,0.5], 0))