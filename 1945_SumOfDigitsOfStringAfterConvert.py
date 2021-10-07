class Solution:
	def getLucky(self, s: str, k : int) -> int:

		res = ""

		for c in s:
			res += str(ord(c) - ord('a') + 1)

		for step in range(0,k):

			res = str(sum(map(int ,res)))

		return res


	def getLucky(self, s: str, k: int) -> int:

		alphabetMap = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, 
		"i":9, "j":1, "k":2, "l":3, "m":4, "n":5, "o":6, "p":7, "q":8, "r":9, 
		"s":10, "t":2, "u":3, "v":4, "w":5, "x":6, "y":7, "z":8}

		sum = 0

		# s to int
		for c in s:
			sum += alphabetMap[c]

		for step in range(1,k):
			temp = 0

			while sum > 0:
				temp += sum % 10
				sum //= 10

			sum = temp

		return sum

