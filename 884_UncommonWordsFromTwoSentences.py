import collections

from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:

        word_map = defaultdict(int)
        res = []

        for s in s1.split():
            word_map[s] += 1
        
        for s in s2.split():
            word_map[s] += 1

        for word in word_map:
            if word_map[word] == 1:
                res.append(word)
        
        return res