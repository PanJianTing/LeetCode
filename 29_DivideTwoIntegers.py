class Solution:
	def divide_5(self, dividend: int, divisor: int) -> int:

		MAX_INT = 2147483647
		MIN_INT = -2147483648
		ans = 0
		isMinus = False

		if dividend < 0:
			isMinus = not isMinus
			dividend = -dividend

		if divisor < 0:
			isMinus = not isMinus
			divisor = -divisor

		if divisor == 1:
			ans = dividend
		elif divisor == 2:
			ans = dividend >> 1
		else:
			maxBit = 1
			temp = divisor
			while dividend >= (temp << 1):
				maxBit += 1
				temp <<= 1

			# 長除法
			for bit in range(maxBit, -1, -1):
				if dividend >= (divisor << bit):
					ans += bit
					dividend -= (divisor << bit)

		if isMinus:
			ans = -ans
			if ans < MIN_INT:
				return MIN_INT
			return ans 
		else:
			if ans > MAX_INT:
				return MAX_INT

		return ans

	def divide_4(self, dividend: int, divisor: int) -> int:

		MAX_INT = 2147483647
		MIN_INT = -2147483648
		ans = 0
		isMinus = False

		if dividend < 0:
			isMinus = not isMinus
			dividend = -dividend

		if divisor < 0:
			isMinus = not isMinus
			divisor = -divisor

		if divisor == 1:
			ans = dividend
		elif divisor == 2:
			ans = dividend >> 1
		else:
			addQ = 1
			temp = divisor
			while dividend >= (temp << 1):
				addQ <<= 1
				temp <<= 1
			
			while dividend >= divisor:
				if dividend >= temp:
					ans += addQ
					dividend -= temp

				addQ >>= 1
				temp >>= 1

		if isMinus:
			ans = -ans
			if ans < MIN_INT:
				return MIN_INT
			return ans 
		else:
			if ans > MAX_INT:
				return MAX_INT

		return ans

	def divide_3(self, dividend: int, divisor: int) -> int:

		MAX_INT = 2147483647
		MIN_INT = -2147483648
		ans = 0
		isMinus = False
		dic = {}

		if dividend < 0:
			isMinus = not isMinus
			dividend = -dividend

		if divisor < 0:
			isMinus = not isMinus
			divisor = -divisor

		if divisor == 1:
			ans = dividend
		elif divisor == 2:
			ans = dividend >> 1
		else:
			addQ = 1
			temp = divisor
			while dividend >= temp:
				dic[addQ] = temp
				addQ <<= 1
				temp <<= 1
			
			allkeys = list(dic.keys())[::-1]
			for key in allkeys:
				if dividend >= dic[key]:
					dividend -= dic[key]
					ans += key

		if isMinus:
			ans = -ans
			if ans < MIN_INT:
				return MIN_INT
			return ans 
		else:
			if ans > MAX_INT:
				return MAX_INT

		return ans


	def divide_2(self, dividend: int, divisor: int) -> int:

		MAX_INT = 2147483647
		MIN_INT = -2147483648
		ans = 0
		isMinus = False

		if dividend < 0:
			isMinus = not isMinus
			dividend = -dividend

		if divisor < 0:
			isMinus = not isMinus
			divisor = -divisor

		if divisor == 1:
			ans = dividend
		elif divisor == 2:
			ans = dividend >> 1
		else:
			while dividend >= divisor:
				addQ = 1
				temp = divisor
				while (temp << 1) < dividend:
					addQ <<= 1
					temp <<= 1

				ans += addQ
				dividend -= temp

		if isMinus:
			ans = -ans
			if ans < MIN_INT:
				return MIN_INT
			return ans 
		else:
			if ans > MAX_INT:
				return MAX_INT

		return ans



class Solution_DP:
	ansTable = {}
	def compute(self, dividend: int, divisor: int, doubleDivisor: int) -> list[int]:

		if dividend < divisor:
			return [0, dividend]
		elif divisor < dividend < doubleDivisor:
			return [1, dividend - divisor]
		elif dividend == divisor:
			return [1, 0]
		elif dividend in self.ansTable:
			return self.ansTable[dividend]
		else:
			# split two part, so T(n) = 2 * T(n/2) + 1 = O(logn)
			left = dividend >> 1
			right = dividend - left

			leftAns = self.compute(left, divisor, doubleDivisor)
			rightAns = self.compute(right, divisor, doubleDivisor)

			q = leftAns[0] + rightAns[0]
			remainder = leftAns[1] + rightAns[1]

			if remainder >= divisor:
				q += 1
				remainder -= divisor
				
			self.ansTable[dividend] = [q ,remainder]

			return [q, remainder]


	def divide(self, dividend: int, divisor: int) -> int:

		MAX_INT = 2147483647
		MIN_INT = -2147483648
		ans = 0
		isMinus = False

		if dividend < 0:
			isMinus = not isMinus
			dividend = -dividend

		if divisor < 0:
			isMinus = not isMinus
			divisor = -divisor

		if divisor == 1:
			ans = dividend
		elif divisor == 2:
			ans = dividend >> 1
		else:
			self.ansTable = {}
			ans = self.compute(dividend, divisor, divisor << 1)[0]


		if isMinus:
			ans = -ans
			if ans < MIN_INT:
				return MIN_INT
			return ans 
		else:
			if ans > MAX_INT:
				return MAX_INT

		return ans