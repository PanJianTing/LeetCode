class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums
        ans.extend(nums)
        return ans

    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums