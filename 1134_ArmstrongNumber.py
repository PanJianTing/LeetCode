import math
class Solution:
    def isArmstrong_my(self, N: int) -> bool:
        nStr = str(N)
        ans = 0
        count = len(nStr)
        
        for n in range(0,count):
            ans += pow(int(nStr[n]), count)
        return ans == N
    
    def isArmstrong(self, N: int) -> bool:
        nStr = str(N)
        ans = 0
        count = len(nStr)
        
        for n in nStr:
            ans += int(n) ** count
        return ans == N

print(Solution.isArmstrong(Solution(), 153))
print(Solution.isArmstrong(Solution(), 123))