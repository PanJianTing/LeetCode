class Solution:
	def numOfStrings(self, patterns: list[str], word: str) -> int:

		result = 0

		for pattern in patterns:
			if pattern in word:
				result += 1
		
		return result