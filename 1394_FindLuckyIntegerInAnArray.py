class Solution:
	def findLucky(self, arr: list[int]) -> int:

		numMap = {}
		result = -1

		for n in arr:
			if n in numMap:
				numMap[n] += 1
			else:
				numMap[n] = 1

		for key in numMap.keys():
			if key == numMap[key]:
				if key > result:
					result = key

		return result