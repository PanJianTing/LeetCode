from functools import cache

class Solution:
    def strangePrinter(self, s: str) -> int:
        N = len(s)
        cur_s = [s[0]]

        for i in range(1, N):
            if cur_s[-1] != s[i]:
                cur_s.append(s[i])
        
        N = len(cur_s)

        @cache
        def dp(st, end):
            if st > end:
                return 0
            
            min_step = 1 + dp(st+1, end)

            for i in range(st+1, end+1):
                if cur_s[st] == cur_s[i]:
                    min_step = min(min_step, dp(st, i-1) + dp(i+1, end))

            return min_step
        
        return dp(0, N-1)
    
    def strangePrinter(self, s: str) -> int:
        N = len(s)
        cur_s = [s[0]]

        for i in range(1, N):
            if s[i] != cur_s[-1]:
                cur_s.append(s[i])

        N = len(cur_s)
        dp = [[0] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 1

        for leng in range(2, N+1):
            for st in range(0, N-leng+1):
                end = st + leng - 1

                dp[st][end] = leng

                for k in range(leng-1):
                    total = dp[st][st+k] + dp[st+k+1][end]
                
                    if cur_s[st+k] == cur_s[end]:
                        total -= 1

                    dp[st][end] = min(dp[st][end], total)

        return dp[0][N-1]


# print(Solution().strangePrinter('aaabbb'))
# print(Solution().strangePrinter('aba'))
# print(Solution().strangePrinter('abab'))
print(Solution().strangePrinter('tbgtgb'))