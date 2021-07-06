class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True

        sIndex = 0
        sCount = len(s)

        for c in t:
            if c == s[sIndex]:
                sIndex += 1
            if sCount == sIndex:
                return True
        
        return False



Solution.isSubsequence(Solution(), "abc", "ahbgdc")
