class Solution:
	def generateParenthesis(self, n: int) -> list[str]:
		if n == 0:
			return [""]
		ans = []
		for c in range(n):
			for left in self.generateParenthesis(c):
				for right in self.generateParenthesis(n-1-c):
					ans.append('({}){}'.format(left, right))

		return ans



class Solution:
	def generateParenthesis(self, n: int) -> list[str]:
		ans = []
		def backtrack(S: list[str], left: int, right: int):
			if len(S) == 2 * n:
				ans.append("".join(S))
			if left < n:
				S.append("(")
				backtrack(S, left + 1, right)
				S.pop()
			if right < left:
				S.append(")")
				backtrack(S, left, right + 1)
				S.pop()
		backtrack([], 0, 0)
		return ans

class Solution:
	def generateParenthesis(self, n: int) -> list[str]:

		ans = []

		def generate(A: list[str]):
			if len(A) == 2*n:
				if valid(A):
					ans.append("".join(A))
			else:
				A.append("(")
				generate(A)
				A.pop()
				A.append(")")
				generate(A)
				A.pop()

		def valid(A: list[str]) -> bool:
			bal = 0
			for c in A:
				if c == "(":
					bal += 1
				else: 
					bal -= 1

				if bal < 0:
					return False

			return bal == 0

		
		generate([])
		return ans




class Solution:
	def generateParenthesis(self, n: int) -> list[str]:

		result = [{"()"}, {"()()", "(())"}]
		now = 2

		while now < n:
			temp = set()
			i = 0
			j = now - 1
			while i <= j:
				left = result[i]
				right = result[j]

				for rp in right:
					for lp in left:
						temp.add(rp + lp)
						temp.add(lp + rp)
						if i == 0:
							temp.add("(" + rp + ")")
				i += 1
				j -= 1

			result.append(temp)
			now += 1

		return list(result[n-1])