import math

class Solution:
    def maximum69Number(self, num: int) -> int:
        ans = 0
        numStr = str(num)
        count = len(numStr)
        isChange = False

        for i in range(0,count):
            if numStr[i] == "6" and isChange == False:
                ans += 9 * pow(10,count-i-1)
                isChange = True
            else:
                ans += int(numStr[i]) * pow(10,count-i-1)
        return ans
    
    
    

print(Solution.maximum69Number(Solution(), 9669))