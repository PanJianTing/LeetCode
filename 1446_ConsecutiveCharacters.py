class Solution:
	def maxPower(self, s: str) -> int:

		maxCount = 0
		beforeChar = ""

		nowCount = 0

		for c in s:

			if beforeChar == c:
				nowCount += 1
			else:
				beforeChar = c
				nowCount = 1

			if nowCount > maxCount:
				maxCount = nowCount

		return maxCount