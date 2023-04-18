from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        minCount = min(len(word1), len(word2))

        index = 0

        res = ""

        while index < minCount:
            res += word1[index]
            res += word2[index]
            index += 1

        res += word1[index:]
        res += word2[index:]
        # while i < len(word1):

        return res
    
    def mergeAlternately(self, word1: str, word2: str) -> str:

        m = len(word1)
        n = len(word2)

        i = 0
        j = 0

        res = []

        while i < m or j < n:
            if i < m:
                res.append(word1[i])
                i += 1
            if j < n:
                res.append(word2[j])
                j += 1
        
        return "".join(res)
    
    def mergeAlternately(self, word1: str, word2: str) -> str:

        m = len(word1)
        n = len(word2)
        maxIndex = max(m, n)
        res = []
        

        for i in range(0, maxIndex):
            if i < m:
                res.append(word1[i])
            if i < n:
                res.append(word2[i])
        
        return "".join(res)

    def mergeAlternately(self, w1: str, w2: str) -> str:

        return "".join(a+b for a, b in zip_longest(w1, w2, fillvalue = ''))
    
            
