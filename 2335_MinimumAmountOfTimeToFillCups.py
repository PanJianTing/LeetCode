class Solution:
    def fillCups(self, amount: list[int]) -> int:
        res = 0
        while 1:

            if amount[0] == 0 and amount[1] == 0 and amount[2] == 0:
                return res
            
            amount.sort()
            if amount[2] > 0:
                amount[2] -= 1
            if amount[1] > 0:
                amount[1] -= 1
            res += 1

            
class Solution:
    def fillCups(self, amount: list[int]) -> int:
        amount.sort()
        return max(amount[2], sum(amount) // 2 + 1)


Solution().fillCups([1,4,2])