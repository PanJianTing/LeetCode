class Solution:
	# 兩種情況：
	# 1. 如果終點比起始大或相等，則經過最多區的為起點到終點的所有section。
	# 2. 如果終點比起始小，則經過最多區的為1~終點的範圍+起點到n的範圍。
	def mostVisited(self, n: int, rounds: list[int]) -> list[int]:

		if rounds[0] <= rounds[-1]:
			return list(range(rounds[0], rounds[-1] + 1))
		res = list(range(1, rounds[-1] + 1))
		res.extend(list(range(rounds[0], n + 1)))

		return res

	def mostVisited_my(self, n: int, rounds: list[int]) -> list[int]:

		visitArray = [0] * (n + 1)


		for i in range(1, len(rounds)):
			start = rounds[i-1]
			end = rounds[i]

			while start != end:

				print(start)
				visitArray[start] += 1

				if start == n:
					start = 1
				else:
					start += 1


		visitArray[rounds[-1]] += 1
		maxVisit = max(visitArray)

		res = []

		for i in range(1, n+1):
			if visitArray[i] == maxVisit:
				res.append(i)

		return res