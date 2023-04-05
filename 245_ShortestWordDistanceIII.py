class Solution:
    def shortestWordDistance(self, wordDict: list[str], word1: str, word2: str) -> int:

        pos1 = -1
        pos2 = -1

        ans = len(wordDict)

        for i, word in enumerate(wordDict):

            if word == word1:
                if word1 == word2 and pos1 != -1:
                    ans = min(ans, i - pos1)
                pos1 = i

            if word == word2:
                pos2 = i

            if pos1 != -1 and pos2 != -1 and word1 != word2:
                ans = min(ans,  abs(pos1 - pos2))

        return ans
    

    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        minimum = n
        w1 = -1
        w2 = -1
        for i in range(n):
            if wordsDict[i] == word1:
                w1 = i
                if w2 != -1:
                    minimum = min(w1 - w2, minimum)
            if wordsDict[i] == word2:
                w2 = i
                if w1 != -1 and w1 != w2:
                    minimum = min(w2 - w1, minimum)
        return minimum
    

class Solution:
    def upper_bound(self, indices: list[int], value: int) -> int:

        left = 0
        right = len(indices) - 1

        index = len(indices)

        while left <= right:
            mid = left + (right - left) >> 1

            if indices[mid] > value:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return index
    

    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:

        indices1 = []
        indices2 = []

        for i, word in enumerate(wordsDict):
            if word1 == word:
                indices1.append(i)
            if word2 == word:
                indices2.append(i)


        shortDistance = len(wordsDict)

        for index in indices1:
            
            x = self.upper_bound(indices2, index)

            if x != len(indices2):
                shortDistance = min(shortDistance, indices2[x] - index)

            if (x != 0) and indices2[x-1] != index:
                shortDistance = min(shortDistance, index - indices2[x-1])

        return shortDistance


    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:

        indices = []

        for i, word in enumerate(wordsDict):

            if word == word1:
                indices.append((i, 0))
            
            if word == word2:
                indices.append((i, 1))

        ans = len(wordsDict)

        for i in range(0, len(indices)-1):

            pos, tag = indices[i]
            
            pos_next, tag_next = indices[i+1]

            if tag != tag_next and pos != pos_next:
                ans = min(ans, pos_next - pos)

        return ans
    
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:

        shortestDistance = len(wordsDict)
        preIndex = -1
        same = word1 == word2

        for i, word in enumerate(wordsDict):
            
            if word == word1 or word == word2:

                if preIndex != -1 and (wordsDict[preIndex] != wordsDict[i] or same):
                    shortestDistance = min(shortestDistance, i-preIndex)

                preIndex = i

        return shortestDistance
