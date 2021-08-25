class Solution:
	def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

		firstCount = 0
		secondCount = 0
		targetCount = 0

		for c in firstWord:
			firstCount = firstCount * 10 + (ord(c) - 97)

		for c in secondWord:
			secondCount = secondCount * 10 + (ord(c) - 97)

		for c in targetWord:
			targetCount = targetCount * 10 + (ord(c) - 97)

		return firstCount + secondCount == targetCount