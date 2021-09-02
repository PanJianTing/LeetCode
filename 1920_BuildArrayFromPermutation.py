class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)

        for i, j in enumerate(nums):
            ans[i] = nums[nums[i]]

        return ans


    def buildArray(self, nums: list[int]) -> list[int]:
        
        ans = []

        for i in range(0, len(nums)):
            ans.append(nums[nums[i]])

        return ans
