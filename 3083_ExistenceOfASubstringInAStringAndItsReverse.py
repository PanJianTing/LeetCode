class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        N = len(s)
        reverse_str = s[::-1]
        for i in range(N-1):
            if s[i:i+2] in reverse_str:
                return True
        return False
    
    def isSubstringPresent(self, s: str) -> bool:
        N = len(s)
        F = set()
        R = set()
        reverse_str = s[::-1]

        for i in range(N-1):
            F.add(s[i:i+2])
            R.add(reverse_str[i:i+2])
        return len(F&R) > 0
    
print(Solution().isSubstringPresent('leetcode'))
print(Solution().isSubstringPresent('abcba'))
print(Solution().isSubstringPresent('abcd'))
print(Solution().isSubstringPresent('aba'))