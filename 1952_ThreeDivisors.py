class Solution:
	def isThree(self, n: int) -> bool:

		# 三個數為，1, n 與 m*m = n的m
		# 1,2,3皆為False
		if n < 4:
			return False

		# 此數必為平方根(m*m = n)(整數)
		if n**0.5 != int(sqrt(n)):
			return False

		# 若還有其他可整除，代表會超過3個
		for i in range(2, int(sqrt(n))):
			if n % i == 0:
				return False
		return True


	def isThree_2(self, n: int) -> bool:
		count = 0
		for i in range(2, n // 2 + 1):
			if n % i == 0:
				count += 1
				if count > 1:
					return False

		return count == 1


	def isThree_1(self, n: int) -> bool:
		count = 0;
		for i in range(2, n):
			if n % i == 0:
				count += 1
				if count > 1:
					return False

		return count == 1


	def isThree_my(self, n: int) -> bool:
		result = 0

		for i in range(1, n):

			if n % i == 0:
				result += 1

		result += 1

		if result == 3:
			return True

		return False