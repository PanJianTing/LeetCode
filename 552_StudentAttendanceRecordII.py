from functools import cache
class Solution:
    def checkRecord(self, n: int) -> int:

        MOD = ((10**9) + 7)
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n)]

        def dp(idx, cur_A, cur_L):
            
            if cur_A >= 2 or cur_L >= 3:
                return 0
            if idx == n:
                return 1
            
            if memo[idx][cur_A][cur_L] != -1:
                return memo[idx][cur_A][cur_L]
            res = 0
            res += dp(idx+1, cur_A, 0) % MOD
            res += dp(idx+1, cur_A, cur_L+1) % MOD
            res += dp(idx+1, cur_A+1, 0) % MOD

            memo[idx][cur_A][cur_L] = res % MOD
            return res % MOD
        
        return dp(0, 0, 0) % MOD
    

    def checkRecord(self, n: int) -> int:

        MOD = ((10**9) + 7)

        @cache
        def dp(idx, cur_A, cur_L):

            if cur_A >= 2 or cur_L >= 3:
                return 0
            
            if idx == n:  
                return 1
            res = 0
            res += dp(idx+1, cur_A, 0) % MOD
            res += dp(idx+1, cur_A, cur_L+1) % MOD
            res += dp(idx+1, cur_A+1, 0) % MOD
                    
            return res % MOD
        return dp(0, 0, 0) % MOD



print(Solution().checkRecord(3))
print(Solution().checkRecord(2))
print(Solution().checkRecord(1))
print(Solution().checkRecord(10101))