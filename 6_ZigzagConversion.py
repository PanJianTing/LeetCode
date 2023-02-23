class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1 or numRows >= len(s):
			return s

		L = [""] * numRows
		index = 0
		# step 往下
		step = 1

		for x in s:
			L[index] += x
			# touch 0 move down
			if index == 0:
				step = 1
			# touch numRows - 1 move up
			elif index == numRows - 1:
				step = -1
			index += step

		return "".join(L)



	def convert(self, s: str, numRows: int) -> str:

		if numRows == 1:
			return s

		shit = numRows + (numRows - 2)

		splitArray = []
		totalStr = len(s) // shit + 1

		for i in range(0, len(s), shit):
			splitArray.append(s[i:i+shit])

		left = 0
		right = shit

		res = "";

		while left <= right:
			for splitStr in splitArray:
				count = len(splitStr)

				if left < count:
					res += splitStr[left]

				if right < count and left != right:
					res += splitStr[right]
			left += 1
			right -= 1

		return res
	
	def convert(self, s: str, numRows: int) -> str:
		isAdd = True
		row = 1
		rowMap = {}

		if numRows == 1:
			return s


		for i in range(0, numRows):
			rowMap[i+1] = ""
			
		for c in s:
			rowMap[row] += c
			if row == numRows:
				isAdd = False
			elif row == 1:
				isAdd = True
				
			if isAdd:
				row += 1
			else:
				row -= 1

		res = ""
		for key in rowMap.keys():
			res += rowMap[key]
        
        # print(res)
		return res