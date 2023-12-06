class Solution:
    def totalMoney(self, n) -> int:
        weeks = n // 7
        remain = n % 7

        weekMoney = ((28 + 28 + 7 * (weeks-1)) * weeks) >> 1
        remainMoney = ((weeks+1 + weeks+remain) * remain) >> 1

        return weekMoney + remainMoney
    

    def totalMoney(self, n) -> int:
        ans = 0
        monday = 0
        while n > 0:
            monday += 1
            for i in range(0, min(n, 7)):
                ans += monday + i
            n -= 7
        return ans
    
print(Solution().totalMoney(4))
print(Solution().totalMoney(10))
print(Solution().totalMoney(20))