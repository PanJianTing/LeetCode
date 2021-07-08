class Solution:
	def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:

		if len(sentence1) != len(sentence2):
			return False

		similarMap = defaultdict(set)
		for a, b in similarPairs:
			similarMap[a].add(b)
			similarMap[b].add(a)

		for i in range(0, len(sentence1)):
			if sentence1[i] == sentence2[i]:
				continue

			if sentence1[i] in similarMap:
				if sentence2[i] in similarMap[sentence1[i]]:
					continue

			if sentence2[i] in similarMap:
				if sentence1[i] in similarMap[sentence2[i]]:
					continue

			return False

		return True

	def areSentencesSimilar_my(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:

		if len(sentence1) != len(sentence2):
			return False

		similarMap = {}

		for pair in similarPairs:
			if pair[0] in similarMap:
				similarMap[pair[0]].append(pair[1])
			else:
				similarMap[pair[0]] = [pair[1]]

			if pair[1] in similarMap:
				similarMap[pair[1]].append(pair[0])
			else:
				similarMap[pair[1]] = [pair[0]]

		print(similarMap)

		for i in range(0, len(sentence1)):
			if sentence1[i] != sentence2[i]:
				if sentence1[i] in similarMap:
					similarList = similarMap[sentence1[i]]
					if sentence2[i] not in similarList:
						return False
				else:
					return False

		return True