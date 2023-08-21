class Solution:
    def repeatedSubstringPattern(self, s):
        N = len(s)
        pattern = ""

        for c in s:
            pattern += c
            temp = pattern
            while len(temp) <= N:
                temp += pattern
                if temp == s:
                    return True
            
        return False
    
    def repeatedSubstringPattern(self, s):
        N = len(s)

        for i in range(1, (N // 2) + 1):
            if N % i == 0:
                pattern = s[:i]
                check = pattern * (N//i)
                if check == s:
                    return True
        return False
    
    def repeatedSubstringPattern(self, s):
        t = s + s
        if s in t[1:-1]:
            return True
        return False
    


print(Solution().repeatedSubstringPattern("abab"))
print(Solution().repeatedSubstringPattern("aba"))
print(Solution().repeatedSubstringPattern("abcabcabcabc"))