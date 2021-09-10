class Solution:

	def specialArray_Not_UNDERSTAND(self, nums: list[int]) -> int:
		nums.sort(reverse=True)
		i = 0
		while i < len(nums) and nums[i] > i:
			i += 1
		return i



	def specialArray(self, nums: list[int]) -> int:

		ans = 0

		while ans <= len(nums):
			count = 0
			for num in nums:
				if num >= ans:
					count += 1
			if count == ans:
				return ans

			ans += 1

		return -1