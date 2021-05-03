from collections import Counter
class Solution:
	def findTheDifference(self, s: str, t: str) -> str:

		diff = 0

		for c in s:
			diff ^= ord(c)

		for c in t:
			diff ^= ord(c)

		return char(diff)




	def findTheDifference(self, s: str, t: str) -> str:

		return list(Counter(t) - Counter(s))[0]


	def findTheDifference_1(self, s: str, t: str) -> str:

		dic = Counter(s)
		
		for c in t:
			if c not in dic or dic[c] == 0:
				return c
			else:
				dic[c] -= 1

		return ""

	def findTheDifference(self, s: str, t: str) -> str:

		dic = {}

		for c in s:
			if c in dic:
				dic[c] += 1
			else:
				dic[c] = 1

		for c in t:
			if c not in dic or dic[c] == 0:
				return c
			else:
				dic[c] -= 1

		return ""


	def findTheDifference(self, s: str, t: str) -> str:

		dic = {}
		difference = ""

		for c in s:
			if c in dic:
				dic[c] += 1
			else:
				dic[c] = 1

		for c in t:
			if c in dic:
				dic[c] -= 1
				if dic[c] == 0:
					del dic[c]
			else:
				difference += c

		for c in dic.keys():

			difference += c



		return difference