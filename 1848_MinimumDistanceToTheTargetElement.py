class Solution:
	def getMinDistance(self, nums: list[int], target: int, start: int) -> int:

		targetIndeies = []
		minDis = float("inf")

		for index in range(0, len(nums)):
			if nums[index] == target:
				minDis = min (minDis, abs(index - start))

		return minDis

	def getMinDistance_my(self, nums: list[int], target: int, start: int) -> int:

		targetIndeies = []
		minDis = 99999

		for index in range(0, len(nums)):
			if nums[index] == target:
				targetIndeies.append(index)


		for index in targetIndeies:
			dis = abs(index - start)
			if dis < minDis:
				minDis = dis

		return minDis