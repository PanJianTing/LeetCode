class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.ans = 0
        
        def dp(cur_0, cur_1):
            if cur_0 + cur_1 > high:
                return
            
            if low <= cur_0 + cur_1:
                    self.ans += 1

            dp(cur_0+zero, cur_1)
            dp(cur_0, cur_1+one)
        dp(0,0)
        return self.ans % (10 ** 9 + 7)
    
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = (10 ** 9) + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        ans = 0
        
        for i in range(1, high+1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= MOD

        for i in range(low, high+1):
            ans += dp[i]
            ans %= MOD
        
        return ans
        

print(Solution().countGoodStrings(3, 3, 1, 1))