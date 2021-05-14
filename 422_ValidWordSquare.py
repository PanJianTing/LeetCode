class Solution:
	def validWordSquare(self, words: list[str]) -> bool:
		for j in range(len(words)):
			for i in range(len(words[j])):

				if i < len(words) and j < len(words[i]):
					if words[j][i] != words[i][j]:
						return False
				else:
					return False
		return True