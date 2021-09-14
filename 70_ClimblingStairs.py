class Solution:
	def climbStairs_step(self, start, end) -> int:
		if start > end:
			return 0

		if start == end:
			return 1

		return self.climbStairs_step(start + 1, end) +  self.climbStairs_step(start + 2, end)


	def climbStairs(self, n: int) -> int:

		return self.climbStairs_step(0, n)


	def climbStairs(self, n: int) -> int:

		if n == 2 or n == 1:
			return n

		stairs = [0] * (n + 1)

		stairs[0] = 0
		stairs[1] = 1
		stairs[2] = 2

		for i in range(3, n+1):
			stairs[i] = stairs[i-2] + stairs[i-1]

		return stairs[n]