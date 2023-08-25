from functools import cache
class Solution:
    def isInterleave(self, s1, s2, s3):
        M = len(s1)
        N = len(s2)

        @cache
        def dp(i, j, res):
            if res == s3 and i == M and j == N:
                return True
            ans = False
            if i < M:
                ans |= dp(i+1, j, res + s1[i])
            if j < N:
                ans |= dp(i, j+1, res + s2[j])
            
            return ans
        
        if M + N != len(s3):
            return False
        
        return dp(0, 0, "")
    
    def isInterleave(self, s1, s2, s3):
        M = len(s1)
        N = len(s2)

        if M+N != len(s3):
            return False
        
        @cache
        def dp(i, j, k):
            if i == M:
                return s2[j:] == s3[k:]
            
            if j == N:
                return s1[i:] == s3[k:]
            
            if  (s3[k] == s1[i] and dp(i+1, j, k+1)) or (s3[k] == s2[j] and dp(i, j+1, k+1)):
                return True
            return False
        
        return dp(0,0,0)
    
    def isInterleave(self, s1, s2, s3):
        M = len(s1)
        N = len(s2)
        if M+N != len(s3):
            return False

        dp = [[False] * (N+1) for _ in range(M + 1)]

        for i in range(M+1):
            for j in range(N+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[M][N]
    
    def isInterleave(self, s1, s2, s3):
        M = len(s1)
        N = len(s2)
        if M+N != len(s3):
            return False

        dp = [False] * (N+1)

        for i in range(M+1):
            for j in range(N+1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i-1] == s3[i-1]
                else:
                    dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])

        return dp[N]
    
print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(Solution().isInterleave("abc", "bcd", "abcbdc"))
print(Solution().isInterleave("aaaa", "aa", "aaa"))
