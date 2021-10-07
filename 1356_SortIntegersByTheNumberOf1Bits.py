class Solution:

	def sortByBits(self, arr: list[int]) -> list[int]:


		return sorted(arr, key=lambda x: (bin(x).count("1"), x))

	def sortByBits(self, arr: list[int]) -> list[int]:
		bitMap = {}
		arr.sort()

		for count in arr:
			bits = bin(count).count("1")

			if bits in bitMap:
				bitMap[bits].append(count)

			else:
				bitMap[bits] = [count]

		allKeys = sorted(bitMap.keys())

		ans = []

		for key in allKeys:
			ans.extend(bitMap[key])

		return ans

	def get1BitsCount(self, count: int) -> int:

		Bits = 0

		while count > 0:
			if count % 2 == 1:
				Bits += 1
			count //= 2

		return Bits


	def sortByBits(self, arr: list[int]) -> list[int]:
		bitMap = {}
		arr.sort()

		for count in arr:
			bits = self.get1BitsCount(count)

			if bits in bitMap:
				bitMap[bits].append(count)

			else:
				bitMap[bits] = [count]

		allKeys = sorted(bitMap.keys())

		ans = []

		for key in allKeys:
			ans.extend(bitMap[key])

		return ans
