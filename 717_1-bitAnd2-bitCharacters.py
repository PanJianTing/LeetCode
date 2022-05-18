class Solution:
	def isOneBitCharacter(self, bits: list[int]) -> bool:

		start = 0

		for index in range(1, len(bits)):

			if index - start > 1 or bits[start] == 0:
				start = index
		return start == (len(bits) - 1)






class Solution:
	def isOneBitCharacter(self, bits: List[int]) -> bool:

		isBeforeOne = False
		queue = []

		for bit in bits[:-1]:

			if bit == 0 and queue == []:
				continue
			else:
				queue.append(bits)

			if len(queue) == 2:
				queue = []

		if queue == []:
			return True
		return False