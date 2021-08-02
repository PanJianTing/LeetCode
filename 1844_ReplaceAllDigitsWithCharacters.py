class Solution:
	def replaceDigits(self, s: str) -> str:

		result = list(s)

		for i in range(1, len(s), 2):
			result[i] = chr(ord(s[i-1]) + int(s[i]))

		return "".join(result)



	def replaceDigits(self, s: str) -> str:

		result = ""

		for i in range(0, len(s)):

			if i % 2 == 0:
				result += s[i]
			else:
				# print(s[i-1], s[i], ord(s[i-1]) + int(s[i]), chr(ord(s[i-1]) + int(s[i])))
				result += chr(ord(s[i-1]) + int(s[i]))


		return result