class Solution:
	def checkPerfectNumber(self, num: int) -> bool:
		
		if num == 1:
			return False

		divisorSum = 1
		left = 2
		right = num - 1

		while left < right:
			if num % left == 0:
				right = num // left
				divisorSum += left + right
			else: 
				right = num // left

			left += 1

		return divisorSum == num

class Solution:
	def checkPerfectNumber(self, num: int) -> bool:

		res = 1
		i = 2
		while i*i < num:
			if num % i == 0:
				res += i + (num // i)
			i+=1

		return res == num

class Solution:
	def checkPerfectNumber(self, num: int) -> bool:

		if num == 1:
			return False

		res = 1
		for i in range(2, (int(num ** 0.5) + 1)):
			if num % i == 0:
				res += i + (num // i)
		return num == res

# 歐拉定理
class Solution:
	def checkPerfectNumber(self, num: int) -> bool:

		# 11不能算，因2^11-1 = 2047 = 23 * 89
		ps = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31]

		for p in ps:
			p_num = (2**(p-1)) * ((2**p) - 1)
			if p_num == num:
				return True
		return False

				
	
Solution().checkPerfectNumber(28)
Solution().checkPerfectNumber(32582657)
Solution().checkPerfectNumber(1)
