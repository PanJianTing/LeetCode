import math

class Solution:

    def valid(self, str:str, base:str) -> bool:        
        k = 1
        check = base * k
        while len(check) <= len(str):
            
            if check == str:
                return True
            k += 1
            check = base * k
        return False
            
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        x = str2
        if len(str1) < len(str2):
            x = str1

        for i in range(len(x), 0, -1):
            base = x[:i]
            # print(base)
            if self.valid(str1, base) and self.valid(str2, base):
                return x[:i]

        return ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 == str2 + str1:
            maxleng = math.gcd(len(str1), len(str2))
            return str1[:maxleng]

        return ""


print(Solution().gcdOfStrings("ABABAB", "ABAB"))
print(Solution().gcdOfStrings("ABCABC", "ABC"))
print(Solution().gcdOfStrings("AA", "A"))         