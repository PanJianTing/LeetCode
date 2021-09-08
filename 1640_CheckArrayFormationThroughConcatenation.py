class Solution:
	def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
		
		elementDic = {}
		
		for i, element in enumerate(arr):
			elementDic[element] = i

		for piece in pieces:
			if len(piece) == 1 and piece[0] not in elementDic:
				return False
			for pIndex in range(len(piece) - 1):
				if piece[pIndex] not in elementDic or piece[pIndex + 1] not in elementDic:
					return False

				if elementDic[piece[pIndex]] + 1 != elementDic[piece[pIndex + 1]]:
					return False
		return True



	def canFormArray_map(self, arr: list[int], pieces: list[list[int]]) -> bool:

		index = 0
		pDic = {}

		for p in pieces:
			pDic[p[0]] = p

		while index < len(arr):
			if arr[index] in pDic:
				piece = pDic[arr[index]]

				for p in piece:
					if p != arr[index]:
						return False
					index += 1
			else:
				return False

		return True


	def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:

		index = 0

		while index < len(arr):
			for piece in pieces:
				if piece[0] == arr[index]:
					break
			else:
				return False

			for p in piece:
				if p != arr[index]:
					return False
				index += 1

		return True