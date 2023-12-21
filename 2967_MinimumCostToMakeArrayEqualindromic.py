from bisect import bisect_right

class Solution:

    def check(self, num) -> bool:
        return str(num)[::-1] == str(num)
        rev = 0
        cur = num
        while cur > 0:
            rev = rev * 10 + cur % 10
            cur //= 10
        
        return num == rev
    
    def getNum1(self, num) -> int:
        
        while (self.check(num) == False):
            num -= 1
        
        return num
    
    def getNum2(self, num) -> int:

        while (self.check(num) == False):
            num += 1
        return num 
    
    def minimumCost(self, nums: list[int]) -> int:

        N = len(nums)
        nums.sort()
        median = nums[N >> 1]

        choose1 = self.getNum1(median)
        choose2 = self.getNum2(median + 1)

        cost1 = 0
        cost2 = 0
        for n in nums:
            cost1 += abs(choose1 - n)
            cost2 += abs(choose2 - n)

        return min(cost1, cost2)
                
    

# print(Solution().minimumCost([107,846,886,574,104,863,476,259,338,647]))
print(Solution().minimumCost([9, 10, 10]))

        