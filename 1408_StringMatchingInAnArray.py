class Solution:
	def stringMatching(self, words: list[str]) -> list[str]:

		result = []

		for i in words:
			for j in words:
				if i != j and i in j and i not in result:
					result.append(i)

		return result



	def stringMatching_my(self, words: list[str]) -> list[str]:

		result = []

		for i in range(0, len(words)):
			for j in range(0, len(words)):
				if i != j:
					if words[i] in words[j]:
						result.append(words[i])
						break

		return result