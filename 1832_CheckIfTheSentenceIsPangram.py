class Solution:
	def checkIfPangram(self, sentence: str) -> bool:

		c = collections.Counter()
		c.update(sentence)

		return len(c) == 26



	def checkIfPangram(self, sentence: str) -> bool:
		return len(set(sentence)) == 26



	def checkIfPangram(self, sentence: str) -> bool:

		if len(sentence) < 26:
			return False

		start = 97

		for i in range(0, 26):
			if chr(start + i) not in sentence:
				return False

		return True