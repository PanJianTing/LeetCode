from functools import cache

class Solution:
    def numDecodings(self, s) -> int:

        allowStr = set()

        for i in range(1, 27):
            allowStr.add(str(i))

        @cache
        def dp(cur):
            if len(cur) == 0:
                return 0
            if cur[0] == "0":
                return 0
            
            if len(cur) == 1 and cur in allowStr:
                return 1
            
            if len(cur) == 2 and cur in allowStr:
                for c in cur:
                    if c not in allowStr:
                        return 1
                return 2
            
            ans = 0
            if cur[0] in allowStr:
                ans += dp(cur[1:])
            if cur[:2] in allowStr:
                ans += dp(cur[2:])
            return ans
        return dp(s)
    
    def numDecodings(self, s) -> int:
        N = len(s)
        
        @cache
        def dp(idx):
            if idx >= N:
                return 1
            if s[idx] == "0":
                return 0
            

            ans = dp(idx+1)
            if 10 <= int(s[idx:idx+2]) <= 26:
                ans += dp(idx+2)
            return ans
        
        return dp(0)
    
    def numDecodings(self, s) -> int:
        N = len(s)
        dp = [0] * (N + 1)

        dp[0] = 1
        dp[1] = 1

        if s[0] == "0":
            dp[1] = 0
        
        for i in range(2, N+1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[N]
    
    def numDecodings(self, s) -> int:
        N = len(s)
        back_one = 1
        back_two = 1

        if s[0] == '0':
            back_one = 0
        
        for i in range(2, N+1):
            cur = 0
            if s[i-1] != '0':
                cur = back_one
            
            if 10 <= int(s[i-2:i]) <= 26:
                cur += back_two
            back_two = back_one
            back_one = cur
        return back_one
    
    def numDecodings(self, s) -> int:
        N = len(s)
        back_one = 1
        back_two = 1

        if s[0] == '0':
            back_one = 0
        
        for i in range(1, N):
            cur = 0
            if s[i] != '0':
                cur = back_one
            
            if 10 <= int(s[i-1:i+1]) <= 26:
                cur += back_two
            back_two = back_one
            back_one = cur
        return back_one

    
print(Solution().numDecodings("12"))
print(Solution().numDecodings("36"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("06"))
print(Solution().numDecodings("11106"))
print(Solution().numDecodings("10"))

        