class Solution:
    def nextGreatestLetter(self, L: list[str], t: str) -> str:

        for l in L:
            if l > t:
                return l
        return L[0]

    def nextGreatestLetter(self, L: list[str], t: str) -> str:

        l = 0
        r = len(L) - 1

        while l <= r:
            mid = (l+r) >> 1
            if L[mid] > t:
                r = mid - 1
            else:
                l = mid + 1

        return L[l % len(L)]
    
    def nextGreatestLetter(self, L: list[str], t: str) -> str:
        l = 0
        r = len(L)

        

        while l < r:
            mid = (l + r) >> 1
            if L[mid] > t:
                r = mid
            else:
                l = mid + 1
        return L[l % len(L)]
    
    
Solution().nextGreatestLetter(["x","x","y","y"], "z")