class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:

        increasing = False
        decreasing = False
        checkCount = len(nums)

        for i in range(1, checkCount):
            if nums[i] > nums[i-1]:
                increasing = True
            elif nums[i] < nums[i-1]:
                decreasing = True

        return not (increasing and decreasing) 