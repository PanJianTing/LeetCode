class Solution:
	def getMaximumGenerated(self, n: int) -> int:
		if n <= 1:
			return n

		result = [0] * (n + 1)

		result[0] = 0
		result[1] = 1

		for i in range(2, n + 1):

			if i % 2 == 0:
				result[i] = result[i//2]
			else:
				result[i] = result[i//2] + result[i//2 + 1]
		return max(result)



	def getMaximumGenerated_my(self, n: int) -> int:

		result = [0] * (n+1)

		i = 0

		while True:
			index = i * 2
			

			if index == 0:
				result[index] = 0
				if index == n:
					break
				result[index + 1] = 1
			else:
				result[index] = result[i]
				if index == n:
					break
				result[index + 1] = result[i] + result[i+1]

			if index + 1 == n:
				break
			i += 1

		return max(result)