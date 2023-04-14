class Solution:

    def lps(self, i: int, j: int, s: str, memo: dict) -> int:

        if (i,j) in memo:
            return memo[(i,j)]

        if i > j:
            return 0

        if i == j:
            return 1
        
        if s[i] == s[j]:
            memo[(i, j)] = 2 + self.lps(i+1, j-1, s, memo)
        else:
            memo[(i, j)] = max(self.lps(i+1, j, s, memo), self.lps(i, j-1, s, memo))
        
        return memo[(i, j)]



    def longestPalindromeSubseq(self, s: str) -> int:
        memo = dict()
        return self.lps(0, len(s)-1, s, memo)
    

    def longestPalindromeSubseq(self, s: str) -> int:

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                print(i,j)
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        print(dp)
        return dp[0][len(s)-1]
    
    def longestPalindromeSubseq(self, s: str) -> int:

        dp = [0 for _ in range(len(s))]
        dpPre = [0 for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            dp[i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[j] = 2 + dpPre[j-1]
                else:
                    dp[j] = max(dpPre[j], dp[j-1])
            
            dpPre = dp[:]

        return dp[len(s)-1]

# Solution().longestPalindromeSubseq("cbbd")
Solution().longestPalindromeSubseq("bbbab")
