from functools import cache


class Solution:
    def numRollsToTarget(self, n, k, target) -> int:
        MOD = (10 ** 9) + 7
        @cache
        def dp(cur, remain):
            if cur == 0:
                if remain == 0:
                    return 1
                else:
                    return 0
            
            ans = 0
            for i in range(1, min(k, remain)+1):
                ans += dp(cur-1, remain - i)
            return ans
        return dp(n, target) % MOD
    
    def numRollsToTarget(self, n, k, target) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (target+1) for _ in range(n+1)]
        
        for i in range(1, min(k, target) + 1):
            dp[1][i] = 1

        for cur in range(2, n+1):
            for t in range(1, target+1):
                way = 0
                for i in range(max(0, t-k), t):
                    way += dp[cur-1][i]
                dp[cur][t] = way
        
        return dp[n][target] % MOD
    
    def numRollsToTarget(self, n, k, target) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (target+1) for _ in range(n+1)]
        
        for i in range(1, min(k, target) + 1):
            dp[1][i] = 1

        for cur in range(2, n+1):
            for t in range(1, target+1):
                dp[cur][t] += dp[cur][t-1] + dp[cur-1][t-1]
                if t > k:
                    dp[cur][t] -= dp[cur-1][t-k-1]
        
        return dp[n][target] % MOD
    

    def numRollsToTarget(self, n, k, target) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (target+1)
        
        for i in range(1, min(k, target) + 1):
            dp[i] = 1

        for _ in range(2, n+1):
            next = [0] * (target+1)
            for t in range(1, target+1):
                next[t] += next[t-1] + dp[t-1]
                if t > k:
                    next[t] -= dp[t-k-1]
            dp = next
        return dp[target] % MOD
    

    def numRollsToTarget(self, n, k, target) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(curIdx, curNum):
            if curIdx == n:
                if curNum == target:
                    return 1
                return 0
            
            ans = 0
            for i in range(1, min(k, target - curNum)+1):
                ans += dp(curIdx+1, curNum + i)
            
            return ans
        return dp(0, 0) % MOD
    
    def numRollsToTarget(self, n, k, target) -> int:
        MOD = 10**9+7
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[n][target] = 1

        for curIdx in range(n-1, -1, -1):
            for curSum in range(0, target+1):
                ways = 0

                for i in range(1, min(k, target-curSum)+1):
                    ways += dp[curIdx+1][curSum + i]

                dp[curIdx][curSum] = ways
        
        return dp[0][0] % MOD

print(Solution().numRollsToTarget(2, 3, 6)) #1
print(Solution().numRollsToTarget(1, 6, 3)) #1
print(Solution().numRollsToTarget(2, 6, 7)) #6
print(Solution().numRollsToTarget(2, 6, 1)) #0
print(Solution().numRollsToTarget(3, 6, 7)) #15
print(Solution().numRollsToTarget(30, 30, 500)) #222616187