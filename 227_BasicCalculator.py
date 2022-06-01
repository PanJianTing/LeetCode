class Solution:
	def calculate(self, s: str) -> int:

		i = 0

		numStack = []

		while i < len(s):
			if s[i].isdigit():
				num = s[i]
				while i+1 < len(s) and s[i+1].isdigit():
					num = num*10+s[i+1]
					i += 1
				numStack.push(num)
		print(numStack)

		return ''

Solution().calculate('2+123+555555')