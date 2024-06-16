from functools import cache

class Solution:
    # MLE
    def maximumTotalDamage(self, power: list[int]) -> int:
        N = len(power)
        power.sort()

        @cache
        def dp(cur, pre):
            if cur == N:
                return 0
            
            if pre < 0 or power[cur] not in [power[pre]+1, power[pre]+2]:
                return max(power[cur] + dp(cur+1, cur), dp(cur+1, pre))
            else:
                return dp(cur+1, pre)
            
        return dp(0, -1)
    
    def maximumTotalDamage(self, power: list[int]) -> int:
        N = len(power)
        power.sort()
        dp = [0] * (N+1)
        j = 0
        max_dp = 0

        for i in range(N):
            if power[i] == power[max(0, i-1)]:
                dp[i+1] = power[i] + dp[i]
            else:
                while(power[j] + 2 < power[i]):
                    j += 1
                    max_dp = max(max_dp, dp[j])
                dp[i+1] = power[i] + max_dp

        return max(dp)
    
    def maximumTotalDamage(self, power: list[int]) -> int:
        N = len(power)
        power.sort()
        dp = [0] * (N)
        dp[0] = power[0]
        max_dp = 0
        idx = 0

        for i in range(1, N):
            if power[i] == power[i-1]:
                dp[i] = dp[i-1] + power[i]
            else:
                while power[idx] + 2 < power[i]:
                    max_dp = max(max_dp, dp[idx])
                    idx += 1
                dp[i] = max_dp + power[i]

        return max(dp)




print(Solution().maximumTotalDamage([1,1,3,4]))
print(Solution().maximumTotalDamage([7,1,6,6]))
print(Solution().maximumTotalDamage([7,1,6,3]))