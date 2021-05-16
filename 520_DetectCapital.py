class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        upperCount = 0

        for c in word:
            if c.isupper():
                upperCount += 1
        
        if upperCount == len(word) or upperCount == 0 or (upperCount == 1 and word[0].isupper()):
            return True

        return False

    def detectCapitalUse_my(self, word: str) -> bool:

        isFirstCapital = False
        upperCount = 0
        lowCount = 0

        for i in range(len(word)):
            if i == 0:
               if word[i].isupper():
                   isFirstCapital = True

            if word[i].isupper():
                upperCount += 1
            else:
                lowCount += 1

        if upperCount == len(word):
            return True
        elif lowCount == len(word):
            return True
        elif isFirstCapital and lowCount == (len(word) - 1):
            return True

        return False
            

# Solution.detectCapitalUse(Solution(), "FlaG")
Solution.detectCapitalUse(Solution(), "ffffffffffffffffffffF")