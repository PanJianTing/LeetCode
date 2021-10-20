class Solution:
	def maxLengthBetweenEqualCharacters(self, s: str) -> int:

		maxLength = -1
		firstDic = {}

		for i in range(0, len(s)):
			if s[i] not in firstDic:
				firstDic[s[i]] = i
			else:
				diff = i - firstDic[s[i]] - 1
				if diff > maxLength:
					maxLength = diff

		return maxLength


	def maxLengthBetweenEqualCharacters(self, s: str) -> int:

		maxLength = -1


		charDic = {}

		for i in range(0, len(s)):
			if s[i] not in charDic:
				charDic[s[i]] = [i, -1]
			else:
				charDic[s[i]][1] = i

		for key in charDic.keys():
			if charDic[key][1] != -1:
				diff = charDic[key][1] - charDic[key][0] - 1
				if diff > maxLength:
					maxLength = diff
				

		return maxLength