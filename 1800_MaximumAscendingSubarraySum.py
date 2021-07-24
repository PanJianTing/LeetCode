class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        before = -1
        maxSum = -1
        sum = 0

        for num in nums:
            if num > before:
                sum += num
            else:
                sum = num
            
            if sum > maxSum:
                maxSum = sum
            before = num
        return maxSum

Solution.maxAscendingSum(Solution(), [10,20,30,5,10,50])

