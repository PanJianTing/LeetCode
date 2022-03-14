class Solution:
	def cellsInRange(self, s: str) -> list[str]:

		colFrom = s[0]
		colTo = s[3]

		rowFrom = s[1]
		rowTo = s[4]

		ans = []

		for col in range(ord(colFrom), ord(colTo) + 1):
			for row in range(int(rowFrom), int(rowTo) + 1):

				sheet = chr(col) + str(row)
				ans.append(sheet)

		return ans

