from functools import cache

class Solution:

    # top down
    def integerBreak(self, n: int) -> int:

        if n <= 3:
            return n - 1
    
        @cache
        def dp(cur):
            if cur <= 3:
                return cur
            
            product = 0
            for i in range(1, cur-1):
                product = max(product, i * dp(cur-i))
            return product


        return dp(n)
    
    # bottom up
    def integerBreak(self, n):
        if n <= 3:
            return n-1
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for cur in range(4, n+1):
            for i in range(1, cur):
                dp[cur]= max(dp[cur], i * dp[cur - i])

        return dp[n]

    def integerBreak(self, n):
        if n <= 3:
            return n - 1
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        return ans * n
    
    def integerBreak(self, n):
        if n <= 3:
            return n-1
        
        if n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** ((n // 3) - 1) * 4
            
        return (3 ** (n // 3)) << 1

    
print(Solution().integerBreak(2))
print(Solution().integerBreak(5))
print(Solution().integerBreak(10))