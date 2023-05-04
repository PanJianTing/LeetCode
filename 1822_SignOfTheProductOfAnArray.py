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
	

class Solution:
	def arraySign(self, nums: list[int]) -> int:
		c = 0
		for num in nums:
			if num == 0:
				return 0
			if num < 0:
				c += 1
		return -1 if c % 2 else 1
	
	def arraySign(self, nums: list[int]) -> int:
		c = 1
		for num in nums:
			if num == 0:
				return 0
			if num < 0:
				c *= -1
		return c
	
	def arraySign(self, nums: list[int]) -> int:
		res = 1
		for num in nums:
			res *= num
		if res < 0:
			return -1
		elif res > 0:
			return 1
		return 0