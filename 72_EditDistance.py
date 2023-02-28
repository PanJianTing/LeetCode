from collections import defaultdict

class Solution:
    memo = defaultdict(int)
    def minDistanceRecur(self, word1: str, word2: str, word1Index: int, word2Index: int) -> int:

        if word1Index == 0:
            return word2Index
        if word2Index == 0:
            return word1Index
        
        if (word1Index, word2Index) in self.memo:
            return self.memo[(word1Index, word2Index)]
        
        if word1[word1Index - 1] == word2[word2Index - 1]:
            return self.minDistanceRecur(word1, word2, word1Index - 1, word2Index - 1)
        else:
            insertOp = self.minDistanceRecur(word1, word2, word1Index, word2Index - 1)
            deleteOp = self.minDistanceRecur(word1, word2, word1Index - 1, word2Index)
            replaceOp = self.minDistanceRecur(word1, word2, word1Index - 1, word2Index - 1)

            ans = min(insertOp, deleteOp, replaceOp) + 1
            self.memo[(word1Index, word2Index)] = ans
            return ans
        
    # top-down: recursion + memory
    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = defaultdict(int)
        return self.minDistanceRecur(word1, word2, len(word1), len(word2))
    
    # bottom-up
    def minDistance(self, word1: str, word2: str) -> int:
        word1L = len(word1)
        word2L = len(word2)

        if word1L == 0:
            return word2L
        if word2L == 0:
            return word1L

        # dp = [[0] * (word2L + 1)] * (word1L + 1)
        dp = [[0] * (word2L + 1) for _ in range((word1L + 1))]

        for i in range(1, word1L + 1):
            dp[i][0] = i

        for i in range(1, word2L + 1):
            dp[0][i] = i

        for i in range(1, word1L + 1):
            for j in range(1, word2L + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[word1L][word2L]

        
print(Solution().minDistance("abc", "abe"))