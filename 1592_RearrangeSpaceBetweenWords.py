class Solution:

	def reorderSpaces(self, text: str) -> str:
		spaceCount = text.count(" ")

		text = text.split()
		
		n = len(text)
		
		splitCount = spaceCount // (n-1) if n > 1 else 0
		
		endSpace = spaceCount - (n-1) * splitCount

		ans = ""

		for i in range(n-1):
			ans += text[i]
			for i in range(splitCount):
				ans += " "

		ans += text[-1]
		for j in range(endSpace):
			ans += " "

		return ans


	def reorderSpaces(self, text: str) -> str:

		words = text.split()
		spaceCount = text.count(" ")

		splitCount = spaceCount
		if len(words) > 1:
			splitCount = spaceCount // (len(words) - 1)


		liftSpace = spaceCount - splitCount * (len(words) - 1)

		print(words, splitCount, liftSpace)

		joinString = ""

		for i in range(splitCount):
			joinString += " "

		result = joinString.join(words)

		if liftSpace > 0:
			for i in range(liftSpace):
				result += " "

		return result

		