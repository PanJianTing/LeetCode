class Solution:
    def doesAliceWin(self, s: str) -> bool:
        check = set(['a', 'e', 'i', 'o', 'u'])
        s = set(s)

        return len(check & s) > 0
    
    def doseAliceWin(self, s: str) -> bool:
        check = set(['a', 'e', 'i', 'o', 'u'])
        for c in s:
            if c in check:
                return True
        return False
    
print(Solution().doesAliceWin("leetcoder"))
print(Solution().doesAliceWin("bbcd"))
        
        
        