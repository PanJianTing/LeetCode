class Solution:
	def intToRoman(self, num: int) -> str:
		thous = num // 1000
		hund = num // 100 % 10
		ten = num % 100 // 10
		one = num % 10

		first = "M" * thous
		second = self.helper(hund, "C", "D", "M")
		third = self.helper(ten, "X", "L", "C")
		last = self.helper(one, "I", "V", "X")

		return first + second + third + last

	def helper(self, num: int, small: int, med: int, big: int) -> str:

		if num <= 3:
			return num * small
		elif num == 4:
			return small + med
		elif num == 5:
			return med
		elif num < 9:
			return med + (num-5) * small
		else:
			return small + big


	def intToRoman(self, num: int) -> str:

		res = ""

		while num > 0:

			if num >= 1000:
				res += "M"
				num -= 1000

			elif num >= 900:
				res += "CM"
				num -= 900

			elif num >= 500:
				res += "D"
				num -= 500

			elif num >= 400:
				res += "CD"
				num -= 400

			elif num >= 100:
				res += "C"
				num -= 100

			elif num >= 90:
				res += "XC"
				num -= 90

			elif num >= 50:
				res += "L"
				num -= 50

			elif num >= 40:
				res += "XL"
				num -= 40

			elif num >= 10:
				res += "X"
				num -= 10

			elif num >= 9:
				res += "IX"
				num -= 9

			elif num >= 5:
				res += "V"
				num -= 5

			elif num >= 4:
				res += "IV"
				num -= 4

			elif num >= 1:
				res += "I"
				num -= 1


		return res







