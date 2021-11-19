class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:

		numsMap = {}

		for i in range(0, len(nums)):
			diff = target - nums[i]
			if diff in numsMap:
				return [i, numsMap[diff]]
			else:
				numsMap[nums[i]] = i

	def twoSum_twoMap(self, nums: list[int], target: int) -> list[int]:
		numsMap = {}

		for i in range(0, len(nums)):
			numsMap[nums[i]] = i

		for i in range(0, len(nums)):
			diff = target - nums[i]
			if diff in numsMap:
				if i != numsMap[diff]:
					return [i, numsMap[diff]]

	def twoSum_BrustForce(self, nums: list[int], target: int) -> list[int]:

		i = 0
		
		numsMap = {}

		for i in range(0, len(nums)):
			if target - nums[i] in nums:
				for j in range(i+1, len(nums)):
					if nums[i] + nums[j] == target:
						return [i , j]