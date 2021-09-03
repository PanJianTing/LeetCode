class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        words = text.split()

        for word in words:
            isType = True
            for c in brokenLetters:
                if c in word:
                    isType = False
            if isType:
                res += 1

        return res