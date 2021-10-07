class Solution:

	def isCovered_1(self, ranges: list[list[int]], left: int, right: int) -> bool:

		for num in range(left, right + 1):
			for lower, upper in ranges:
				if lower <= num <= upper:
					break
			else:
				return False
		return True

	def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
		while left <= right:
			for ragne in ranges:
				if ragne[0] <= left <= ragne[1]:
					break
			else:
				return False

			left += 1


		return True