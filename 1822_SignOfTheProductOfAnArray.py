class Solution:
	def arraySign(self, nums: list[int]) -> int:

		if 0 in nums:
			return 0

		if str(nums).count("-") % 2 == 0:
			return 1

		return -1


	def arraySign_my(self, nums: list[int]) -> int:

		result = 1

		for n in nums:
			result *= n

		if result == 0:
			return 0
		elif result > 0:
			return 1

		return -1