class Solution:
	def trailingZeroes(self, n: int) -> int:

		nFactorial = 1
		result = 0

		while n > 0:
			nFactorial *= n;
			n -= 1

		while nFactorial > 0:
			if nFactorial % 10 == 0:
				result += 1
				nFactorial //= 10
			else:
				return result
		
		return result