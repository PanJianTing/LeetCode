class Solution:
	def checkRecord(self, s: str) -> bool:
		countA = 0
		for c in s:
			if c == "A":
				countA += 1

		return countA < 2 and "LLL" not in s



	def checkRecord_my(self, s: str) -> bool:

		countA = 0
		countL = 0
		beforeL = False

		for c in s:
			if c == "L":
				beforeL = True
				countL += 1
			else:
				if c == "A":
					countA += 1
				if countL < 3:
					beforeL = False
					countL = 0
		print(countA, countL)
		return countA < 2 and countL < 3 
