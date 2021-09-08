class Solution:
	def areOccurrencesEqual(self, s: str) -> bool:

		return len(set(Counter(s).values())) == 1

	def areOccurrencesEqual(self, s: str) -> bool:

		sentanceMap = {}

		for c in s:
			if c in sentanceMap:
				sentanceMap[c] += 1
			else:
				sentanceMap[c] = 1

		return len(set(sentanceMap.values())) == 1