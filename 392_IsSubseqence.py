from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        M = len(s)
        N = len(t)
        p1 = 0
        p2 = 0
            
        while p1 < M and p2 < N:
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        
        return p1 == M
    
    def isSubsequence(self, s, t):
        M = len(s)
        N = len(t)

        def dp(i, j):
            if i == -1:
                return True
            
            if j == -1:
                return False
            
            if s[i] == t[j]:
                return dp(i-1, j-1)
            return dp(i, j-1)

        return dp(M-1, N-1)
    
    def isSubsequence(self, s, t):
        M = len(s)
        N = len(t)

        def dp(i, j):
            if i == M:
                return True
            
            if j == N:
                return False
            
            if s[i] == t[j]:
                return dp(i+1, j+1)
            return dp(i, j+1)
        return dp(0,0)
    

    def isSubsequence(self, s, t):
        M = len(s)
        N = len(t)

        char_dict = defaultdict(list)

        for i, char in enumerate(t):
            char_dict[char].append(i)

        curidx = -1
        for char in s:
            haveMatch = False
            for idx in char_dict[char]:
                if curidx < idx:
                    curidx = idx
                    haveMatch = True
                    break

            if haveMatch == False:
                return False
        return True
    
    def isSubsequence(self, s, t):

        M = len(s)
        N = len(t)

        dp = [[0] * (N+1) for _ in range(M+1)]

        for i in range(1, M+1):
            for j in range(1, N+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[M][N] == M
        
        
print(Solution().isSubsequence("abc", "ahbgdc"))
print(Solution().isSubsequence("axc", "ahbgdc"))
print(Solution().isSubsequence("", "ahbgdc"))