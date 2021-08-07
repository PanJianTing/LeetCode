class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        result = ""
        numberSet = set()

        for c in word:
            if c.isnumeric():
                result += c
            else:
                if len(result) > 0:
                    numberSet.add(int(result))
                result = ""
        if len(result) > 0:
            numberSet.add(int(result)) 
        return len(numberSet)


# Solution.numDifferentIntegers(Solution(), "a123bc34d8ef34")
Solution.numDifferentIntegers(Solution(), "leet1234code234")
""