from functools import lru_cache
from collections import Counter

class Solution:
    def numWays(self, words: list[str], target: str) -> int:

        alphabet = 26
        mod = 10 ** 9 + 7
        m = len(target)
        n = len(words)
        k = len(words[0])
        cnt = [[0 for _ in range(k)] for _ in range(alphabet)]
        dp = [[0 for _ in range(k+1)] for _ in range(m+1)]
        dp[0][0] = 1

        for i in range(k):
            for s in words:
                index = ord(s[i]) - ord('a')
                cnt[index][i] += 1

        for i in range(m+1):
            for j in range(k):
                if i < m:
                    index = ord(target[i]) - ord('a')
                    dp[i+1][j+1] += cnt[index][j] * dp[i][j]
                dp[i][j+1] += dp[i][j]

        return dp[m][k] % mod
    

    def numWays(self, words: list[str], target: str) -> int:

        n = len(target)
        mod = 10 ** 9 + 7
        res = [1] + [0] * n

        for i in range(len(words[0])):
            count = Counter(w[i] for w in words)
            for j in range(n-1, -1, -1):
                res[j+1] += res[j] * count[target[j]]
        
        return res[n] % mod



        


    
print(Solution().numWays(["acca","bbbb","caca"], "aba"))
# 
# print(Solution().numWays(["a","b","a"], "b"))