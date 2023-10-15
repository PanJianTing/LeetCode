from functools import cache

class Solution:
    MOD = 10**9 + 7
    def numWays(self, step: int, arrLen: int) -> int:
        arrLen = min(step, arrLen)

        @cache
        def dp(cur, remain):
            if remain == 0:
                if cur == 0:
                    return 1
                else:
                    return 0
            ans = dp(cur, remain-1)
            if cur > 0:
                ans += dp(cur-1, remain-1)
            if cur < arrLen-1:
                ans += dp(cur+1, remain-1)
            
            return ans
        
        return dp(0, step) % (10**9+7)
    
    def numWays(self, step: int, arrLen: int) -> int:
        arrLen = min(arrLen, step)
        dp = [[0] * arrLen for _ in range(step+1)]

        dp[0][0] = 1

        for i in range(1, step+1):
            for j in range(arrLen-1, -1, -1):
                dp[i][j] = dp[i-1][j]
                if j < arrLen-1:
                    dp[i][j] += dp[i-1][j+1]
                if j > 0:
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[step][0] % ((10**9) + 7)
    

    def numWays(self, step, arrLen) -> int:
        arrLen = min(arrLen, step)
        dp = [0] * arrLen

        dp[0] = 1

        for _ in range(1, step+1):
            temp = [0] * arrLen
            for j in range(arrLen-1, -1, -1):
                temp[j] = dp[j]
                if j > 0:
                    temp[j] += dp[j-1]
                if j < arrLen-1:
                    temp[j] += dp[j+1]
            dp = temp
        return dp[0] % (10**9 + 7)
    

    def numWays(self, step, arrLen) -> int:
        arrLen = min(step, arrLen)
        MOD = 10**9 + 7
        dp = [0, 1]

        for i in range(step):
            print(min(arrLen+1, i+3))
            # print("---")
            dp[1:] = [sum(dp[i-1: i+2]) for i in range(1, min(arrLen+1, i+3))] + [0]
        return dp[1] % MOD
    
    def numWays(self, step, arrLen) -> int:
        arrLen = min(step // 2 + 1, arrLen)
        MOD = 10**9 + 7
        dp = [1] + [0] * arrLen

        for _ in range(step):
            pre = 0
            for i in range(arrLen):
                dp[i], pre = (pre + dp[i] + dp[i+1]), dp[i]

        return dp[0] % MOD

print("=============")
print(Solution().numWays(3,2))
print("=============")
print(Solution().numWays(2,4))
print("=============")
print(Solution().numWays(4,2))
print("=============")