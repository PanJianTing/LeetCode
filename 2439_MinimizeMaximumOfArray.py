class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:

        ans = 0
        prefixSum = 0

        for i, num in enumerate(nums):
            prefixSum += num
            ans = max(ans, (prefixSum + i) // (i+1))

        return ans