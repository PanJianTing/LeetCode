from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M = len(text1)
        N = len(text2)

        dp = [[0] * (N+1) for _ in range(M+1)]

        for i in range(0, M):
            for j in range(0, N):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return max(dp[M])
    

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M = len(text1)
        N = len(text2)

        dp = [0] * (N+1)

        for i in range(M):
            temp = [0] * (N+1)
            for j in range(N):
                if text1[i] == text2[j]:
                    temp[j+1] = dp[j] + 1
                else:
                    temp[j+1] = max(dp[j+1], temp[j])
        
            dp = temp

        return max(dp)
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M = len(text1)
        N = len(text2)

        @cache
        def dp(i, j):
            if i == M or j == N:
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            return max(dp(i+1, j), dp(i, j+1))
        
        return dp(0,0)
    


print(Solution().longestCommonSubsequence("abcde", "ace"))
print(Solution().longestCommonSubsequence("abc", "abc"))
print(Solution().longestCommonSubsequence("abc", "def"))
