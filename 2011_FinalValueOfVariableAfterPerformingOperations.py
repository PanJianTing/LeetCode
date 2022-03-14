class Solution:
	def finalValueAfterOperations(self, operations: list[str]) -> int:

		ans = 0

		for op in operations:
			if "++X" == op or "X++" == op:
				ans += 1
			else:
				ans -= 1
		return ans