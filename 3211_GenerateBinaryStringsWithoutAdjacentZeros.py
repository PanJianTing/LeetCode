from collections import defaultdict
import heapq

class Solution:
    def validStrings(self, n: int) -> list[str]:
        if n == 1:
            return ['0', '1']

        res = []
        
        def getStr(pre, cur):
            if len(cur) == n:
                res.append(cur)
                return
            if pre == 1:
                getStr(0, cur+"0")
            getStr(1, cur+"1")
        
        getStr(0, '0')
        getStr(1, '1')
        return res
    

    def validStrings(self, n: int) -> list[str]:
        valid = ['0', '1']

        for _ in range(1, n):
            temp = []
            for s in valid:
                if s[-1] == '1':
                    temp.append(s+'0')
                temp.append(s+'1')
            valid = temp
        return valid
        
    
print(Solution().validStrings(2))
print(Solution().validStrings(3))
# print(Solution().validStrings(18))