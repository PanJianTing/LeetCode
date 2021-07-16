class Solution:
	def prefixesDivBy5_2_fast(self, nums: list[int]) -> list[bool]:
		val = 0
		sumList = [nums[0]]

		for i in range(1, len(nums)):
			sumList.append( (nums[i] + sumList[i-1] * 2) % 5)

		return [x == 0 for x in sumList]

	def prefixesDivBy5_1_fast(self, nums: list[int]) -> list[bool]:
		val = 0
		sumList = [nums[0]]

		for i in range(1, len(nums)):
			sumList.append(nums[i] + sumList[i-1] * 2)

		return [x % 5 == 0 for x in sumList]


	def prefixesDivBy5_1(self, nums: list[int]) -> list[bool]:

		val = 0
		result = []

		for num in nums:
			val = (val << 1) + num
			result.append(val % 5 == 0)

		return result



	# timeout
	def prefixesDivBy5_timeout(self, nums: list[int]) -> list[bool]:

		now = 0
		digitList = []
		result = []

		for num in nums:
			digitList.append(num)

			if sum(digitList) % 5 == 0:
				result.append(True)
			else:
				result.append(False)

			digitList *= 2

		return result
