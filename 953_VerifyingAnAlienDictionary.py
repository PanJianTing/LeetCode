class Solution:
    def isValidWord(self, str1: str, str2: str, orderDic:dict) -> bool:

        len1 = len(str1)
        len2 = len(str2)
        maxLeng = min(len1, len2)
        for i in range(0, maxLeng):
            if orderDic[str1[i]] > orderDic[str2[i]]:
                return False
            elif orderDic[str1[i]] < orderDic[str2[i]]:
                return True
                    
        if len1 > len2:
            return False      

        return True

    def isAlienSorted(self, words:list[str], order: str) -> bool:
        orderDic = {}

        for i in range(0, len(order)):
            orderDic[order[i]] = i

        for i in range(0, len(words)-1):
            if self.isValidWord(words[i], words[i+1], orderDic) == False:
                return False

        return True

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:

        m = {c:i for i,c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


print(Solution().isAlienSorted(["hello","leetcode"], 'hlabcdefgijkmnopqrstuvwxyz'))
print(Solution().isAlienSorted(["word","world","row"], 'worldabcefghijkmnpqstuvxyz'))
print(Solution().isAlienSorted(["apple","app"], 'abcdefghijklmnopqrstuvwxyz'))