class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (right + left) >> 1

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return left
