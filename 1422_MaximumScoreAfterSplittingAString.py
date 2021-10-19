class Solution:
	def maxScore(self, s: str) -> int:

		r0, r1 = s.count("0"), s.count("1")
		l0, l1 = 0,0

		m = len(s)
		maxSum = 0

		for i in range(m-1):
			if s[i] == "0":
				r0 -= 1
				l0 += 1
			else:
				r1 -= 1
				l1 += 1
			maxSum = max(maxSum, l0 + r1)

		return maxSum



class Solution:
	def maxScore(self, s: str) -> int:

		leftSide = list(s[0])
		rightSide = list(s[1:])

		nowLeftZero = 0
		nowRightOne = 0

		maxSum = 0

		for c in leftSide:
			if c == '0':
				nowLeftZero += 1

		for c in rightSide:
			if c == '1':
				nowRightOne += 1


		maxSum = nowLeftZero + nowRightOne

		while len(rightSide) > 1:
			shift = rightSide[0]

			if shift == '0':
				nowLeftZero += 1
			else:
				nowRightOne -= 1

			maxSum = max(maxSum, nowLeftZero + nowRightOne)

			del rightSide[0]

		return maxSum