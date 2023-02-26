from functools import cache

class Solution:
    @cache
    def minDistanceRecur(self, word1: str, word2: str, word1Index: int, word2Index: int) -> int:

        if word1Index == 0:
            return word2Index
        if word2Index == 0:
            return word1Index
        
        if word1[word1Index - 1] == word2[word2Index - 1]:
            return self.minDistanceRecur(word1, word2, word1Index - 1, word2Index - 1)
        else:
            insertOp = self.minDistanceRecur(word1, word2, word1Index, word2Index - 1)
            deleteOp = self.minDistanceRecur(word1, word2, word1Index - 1, word2Index)
            replaceOp = self.minDistanceRecur(word1, word2, word1Index - 1, word2Index - 1)

            return min(insertOp, deleteOp, replaceOp) + 1

    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistanceRecur(word1, word2, len(word1), len(word2))

        
print(Solution().minDistance("abc", "abe"))