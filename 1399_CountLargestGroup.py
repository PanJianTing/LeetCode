class Solution:

	def sumOfDigit(self, n: int) -> int:

		digitSum = 0
		while n > 0:
			digitSum += n%10
			n = n//10

		return digitSum

	def countLargestGroup(self, n: int) -> int:
		countMap = {}

		for i in range(1, n+1):
			digitSum = self.sumOfDigit(i)

			if digitSum in countMap:
				countMap[digitSum] += 1
			else:
				countMap[digitSum] = 1

		maxCount = 0

		result = 0

		for key in countMap.keys():
			if countMap[key] > maxCount:
				maxCount = countMap[key]
				result = 0
			if countMap[key] == maxCount:
				result += 1
		return result
