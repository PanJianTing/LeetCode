class Solution:
	def findMiddleIndex(self, nums: list[int]) -> int:
		rightSum = sum(nums)
		leftSum = 0

		for i in range(len(nums)):

			if leftSum == rightSum - nums[i]:
				return i 
			leftSum += nums[i]
			rightSum -= nums[i]

		return -1




	def findMiddleIndex(self, nums: list[int]) -> int:

		for i in range(len(nums)):
			left = nums[0:i]
			right = nums[i+1:]

			if sum(left) == sum(right):
				return i
		return -1