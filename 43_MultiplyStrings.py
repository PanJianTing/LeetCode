from itertools import zip_longest
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        answer = [0] * (len(num1) + len(num2))
        
        firstNum = num1[::-1]
        secondNum = num2[::-1]
        
        for firstIndex, d1 in enumerate(firstNum):
            for secondIndex, d2 in enumerate(secondNum):
                index = firstIndex + secondIndex
                
                res = int(d1) * int(d2) + answer[index]
                
                carray = res // 10
                res = res % 10
                
                answer[index] = res
                answer[index + 1] += carray
                
        if answer[-1] == 0:
            answer.pop()
            
        return "".join(str(digit) for digit in reversed(answer))


class Solution:
	def multiply(self, num1: str, num2: str):

		if num1 == "0" or num2 == "0":
			return "0"


		answer = [0] * (len(num1) + len(num2))

		firstNum = num1[::-1]
		sencondNum = num2[::-1]

		for index, digit in enumerate(sencondNum):
			answer = self.addTwoNum(self.multiplyOneDigit(firstNum, int(digit), index), answer)
			
		if answer[-1] == 0:
		    answer.pop()
		return ''.join(str(s) for s in reversed(answer))
			

	def multiplyOneDigit(self, multiNum: str, digit: int, zero: int):

		result = [0] * (len(multiNum) + 1)

		for index, m1 in enumerate(multiNum):

			carry = result[index]
			ans = int(m1) * digit + carry

			carry = ans // 10
			ans = ans % 10

			result[index] = ans
			result[index + 1] = carry

		for index in range(0, zero):
		    result.insert(0, 0)
		
		if result[-1] == 0:
		    result.pop()
		return result
		
	def addTwoNum(self, num1: list, num2: list):
	    carry = 0
	    answer = []
	    for d1, d2 in zip_longest(num1, num2, fillvalue=0):
	        allSum = d1+d2+carry
	        carry = allSum // 10
	        allSum = allSum % 10
	        
	        answer.append(allSum)
	    return answer




class Solution:
	def multiply(self, num1: str, num2: str) -> str:

		if num1 == "0" or num2 == "0":
			return "0"

		if len(num1) < len(num2):
			num1, num2 = num2, num1

		addArray = []
		fixZero = 0

		# multiply
		for i in range(len(num2)-1, -1, -1):
			ansStr = ""
			carry = 0
			m2 = int(num2[i])
			
			for j in range(len(num1)-1, -1, -1):

				m1 = int(num1[j])

				ans = m1 * m2 + carry

				carry = ans // 10
				ans %= 10
				ansStr = str(ans) + ansStr

			if carry > 0:
				ansStr = str(carry) + ansStr

			for j in range(0, fixZero):
				ansStr += "0"

			addArray.append(ansStr)
			fixZero += 1

		# add

		addAllStr = addArray[0]

		for i in range(1, len(addArray)):
			addStr = addArray[i]

			if len(addAllStr) < len(addStr):
				fix = len(addStr) - len(addAllStr)
				for index in range(0, fix):
					addAllStr = "0" + addAllStr

			carry = 0
			newAddStr = ""
			for j in range(len(addAllStr)-1, -1, -1):

				m1 = addStr[j]

				m2 = addAllStr[j]

				ans = int(m1) + int(m2) + carry

				carry = ans // 10
				ans %= 10

				newAddStr = str(ans) + newAddStr

			if carry > 0:
				newAddStr = str(carry) + newAddStr

			addAllStr = newAddStr

		return addAllStr