class Solution:
	def checkPerfectNumber(self, num: int) -> bool:

		divisorSum = 1
		left = 2
		right = num - 1

		while left < right:
			print(left, right)
			if num % left == 0:
				right = num // left
				divisorSum += left + right

			left += 1

		return divisorSum == num