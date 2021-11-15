# dp
class Solution:

	matrixDic = {}

	def getNum(self, col: int, row: int) -> int:

		if col == 0 or row == 0 or col == row:
			return 1
		else:
			dicIndex = col * 10 + row
			
			if dicIndex in self.matrixDic:
				return self.matrixDic[dicIndex]
			
			temp = self.getNum(col-1, row-1) + self.getNum(col-1, row)
			self.matrixDic[dicIndex] = temp
			print(self.matrixDic)
			
			return temp

	def getRow(self, rowIndex: int) -> list[int]:

		ans = []
		self.matrixDic = {}

		for i in range(0, rowIndex + 1):
			ans.append(self.getNum(rowIndex, i))

		return ans

# normal
class Solution:
	def getRow(self, rowIndex: int) -> list[int]:

		matrix = []

		for j in range(0, rowIndex + 1):
			temp = []
			for i in range(0, rowIndex + 1):
				temp.append(1)
			matrix.append(temp)



		for j in range(1,rowIndex + 1):
			for i in range(1, rowIndex + 1):
				matrix[j][i] = matrix[j-1][i] + matrix[j][i-1]


		result = []

		for i in range(rowIndex , -1 , -1):
			j = rowIndex - i

			result.append(matrix[j][i])

		return result

