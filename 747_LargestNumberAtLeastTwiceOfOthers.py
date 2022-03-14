class Solution:
	def dominantIndex(self, nums: list[int]) -> int:

		index = 0
		maxnum = 0
		second = 0

		for i, n in enumerate(nums):
			if n > maxnum:
				second = maxnum
				maxnum = n
				index = i
			elif n > second:
				second = n

		return index if maxnum > second * 2 else -1

	def dominantIndex(self, nums: list[int]) -> int:

		maxnum = max(nums)
		index = 0

		for i in range(0, len(nums)):
			if nums[i] == maxnum:
				index = i



		for n in nums:
			if n * 2 > maxnum and maxnum != n:
				return -1

		return index