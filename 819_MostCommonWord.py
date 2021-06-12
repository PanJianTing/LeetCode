import re
from typing import DefaultDict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[int]) -> str:

        bannedSet = set(banned)
        result = ""
        max = -1
        word = ""
        wordMap = DefaultDict(int)


        for i, c in enumerate(paragraph):
            if c.isalnum():
                word += c.lower()
                if i != len(paragraph) -1:
                    continue

            if len(word) > 0:
                if word not in bannedSet:
                    wordMap[word] += 1
                    if wordMap[word] > max:
                        result = word
                        max = wordMap[word]
                word = ""
        
        return result



    def mostCommonWord_my(self, paragraph: str, banned: list[int]) -> str:
        paragraph = re.sub("[!?',;.]", " ", paragraph)
        wordMap = {}

        for word in paragraph.split(" "):
            # print(word)
            if word == "":
                continue
            word = word.lower()
            if word in wordMap:
                wordMap[word] += 1
            else:
                wordMap[word] = 1
        
        max = -1
        result = ""
        for word in wordMap.keys():
            if wordMap[word] > max and word not in banned:
                max = wordMap[word]
                result = word
        return result


Solution.mostCommonWord(Solution(), "Bob. hIt, baLl", ["bob", "hit"])

Solution.mostCommonWord(Solution(), "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])


