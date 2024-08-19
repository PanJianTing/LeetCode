from functools import cache

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        @cache
        def dp(cur, cur_s, cur_paste):
            if cur_s > n:
                return float('inf')
            if cur_s == n:
                return cur
            if cur_paste == 0:
                return dp(cur+1, cur_s, cur_s)
            if cur_s <= cur_paste:
                return dp(cur+1, cur_s + cur_paste, cur_paste)
            return min(dp(cur+1, cur_s + cur_paste, cur_paste), dp(cur+1, cur_s, cur_s))
        
        return dp(0, 1, 0)
    
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        @cache
        def dp(cur_l, cur_paste):
            if cur_l == n:
                return 0
            if cur_l > n:
                return float('inf')
            
            return min(2 + dp(cur_l << 1, cur_l), 1 + dp(cur_l+cur_paste, cur_paste))
        
        return 1 + dp(1, 1)
    

    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[1] = 0

        for i in range(2, n+1):
            for j in range(1,(i>>1)+1):

                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        
        return dp[n]
    

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        cur_l = 1
        cur_paste = 1
        res = 1

        while cur_l != n:
            if n % cur_l == 0 and cur_l != cur_paste:
                cur_paste = cur_l
            else:
                cur_l += cur_paste
            
            res += 1
        return res

        
    
# print(Solution().minSteps(1))
# print(Solution().minSteps(2))
# print(Solution().minSteps(3))
# print(Solution().minSteps(4))
# print(Solution().minSteps(5))
print(Solution().minSteps(10))
print(Solution().minSteps(1000))