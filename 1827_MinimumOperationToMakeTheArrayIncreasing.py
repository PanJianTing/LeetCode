class Solution:
	def minOperations(self, nums: list[int]) -> int:

		op = 0

		for i in range(1, len(nums)):

			count = nums[i]
			before = nums[i-1]

			if before < count:
				continue
			else:
				op += before - count + 1
				nums[i] = before + 1

		return op