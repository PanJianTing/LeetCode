import collections

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:

        s1 = collections.Counter(s1.split(" "))
        s2 = collections.Counter(s2.split(" "))

        result = []

        for key in s1.keys():
            if s1[key] == 1 and key not in s2:
                result.append(key)

        for key in s2.keys():
            if s1[key] == 1 and key not in s1:
                result.append(key)

        return result


    def uncommonFromSentences_my(self, s1: str, s2: str) -> list[str]:

        wordMap = {}

        s1 = s1.split(" ")
        s2 = s2.split(" ")

        for word in s1:
            if word in wordMap:
                wordMap[word] = 0
            else:
                wordMap[word] = 1
        
        for word in s2:
            if word in wordMap:
                wordMap[word] = 0
            else:
                wordMap[word] = 1

        return [word for word in wordMap if wordMap[word] == 1]
