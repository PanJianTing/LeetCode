class Solution:

    def makeGood(self, s: str) -> str:
        
        sList = []

        for c in s:
            if sList and abs(ord(sList[-1]) - ord(c)) == 32:
                sList.pop()
            else:
                sList.append(c)
        return "".join(sList)

    def makeGood(self, s: str) -> str:
        
        isGood = False

        while isGood == False:
            isGood = True
            for i in range(0, len(s)-1):
                before = s[i]
                after = s[i+1]
                if (before != after) and (after.upper() == before or after == before.upper()):
                    s = s[0:i] + s[i+2:]
                    isGood = False
                    break

        return s

Solution.makeGood(Solution(), "kkdsFuqUfSDKK")



            



        