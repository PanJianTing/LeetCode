from functools import cache

class Solution:
    def getRow(self, rowIdx) -> list[int]:

        if rowIdx == 0:
            return [1]
        
        now = [1, 1]
        for _ in range(1, rowIdx):
            temp = []
            for i in range(0, len(now)-1):
                temp.append(now[i] + now[i+1])
            now = [1] + temp + [1]
        
        return now
    
    def getRow(self, rowIdx) -> list[int]:
        ans = []

        @cache
        def getNum(rowIdx, colIdx):
            if rowIdx == 0 or colIdx == 0 or rowIdx == colIdx:
                return 1
            
            return getNum(rowIdx-1, colIdx-1) + getNum(rowIdx-1, colIdx)
        
        for i in range(0, rowIdx + 1):
            ans.append(getNum(rowIdx, i))
        
        return ans
    
    def getRow(self, rowIdx) -> list[int]:
        ans = [1] * (rowIdx + 1)

        for i in range(2, rowIdx+1):
            for j in range(i-1, 0, -1):
                ans[j] = ans[j-1]+ ans[j]

        return ans
    
    def getRow(self, rowIdx) -> list[int]:
        ans = [1]

        for i in range(1, rowIdx+1):
            ans.append((ans[i-1] * (rowIdx-i+1)) // i)

        return ans


print(Solution().getRow(0))
print(Solution().getRow(1))  
print(Solution().getRow(2))  
print(Solution().getRow(3))
print(Solution().getRow(4))
