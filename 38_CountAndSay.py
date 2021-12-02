class Solution:
	def countAndSay(self, n: int) -> str:
		result = ["1"]

		i = 2

		while i <= n:
			result.append(self.say(result[i-2]))
			i += 1

		return result[-1]

	def say(self, num: str) -> str:
		current = None
		count = 0
		output = ""

		for ch in num:
			if current != ch:
				if current:
					output += f"{count}{current}"
				current = ch
				count = 1
			else:
				count += 1
		output += f"{count}{current}"
		return output


	def countAndSay(self, n: int) -> str:

		if n == 1:
			return "1"

		say = "1."

		for _ in range(2,n+1):

			# print(say)
			count = 0
			newSay = ""
			for i in range(0, len(say)-1):
				c = say[i]
				after = say[i+1]
				if c == after:
					count += 1
				else:
					newSay += f"{count+1}{c}"
					count = 0
			say = newSay + "."

		return say[0:-1]