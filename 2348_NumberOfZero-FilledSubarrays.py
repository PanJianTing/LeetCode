class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:

        count = 0
        ans = 0
        nums.append(1)

        for num in nums:
            if num == 0:
                count += 1
            else:
                ans += ((1+count) * count) >> 1
                count = 0
        return ans
    
class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        count = 0
        ans = 0

        for num in nums:
            if num:
                count = 0
            else:
                count += 1
            ans += count
        return ans