class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:

		splitArray = s.split(" ")

		matchDic = {}

		if len(splitArray) != len(pattern):
			return False

		for i in range(0, len(pattern)):
			matchDic[pattern[i]] = None

		for i in range(0, len(splitArray)):
			word = splitArray[i]
			p = pattern[i]
			if matchDic[p] is not None:
				if matchDic[p] != word:
					return False
			else:
				matchDic[p] = word

		wordArray = []

		for key in matchDic.keys():

			if matchDic[key] in wordArray:
				return False
			else:
				wordArray.append(matchDic[key])


		return True