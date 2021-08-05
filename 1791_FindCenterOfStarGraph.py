class Solution:
	# 只判斷前兩個點，取兩個點共有的
	def findCenter(self, edges: list[list[int]]) -> int:
		#取前兩點做set，做交集。
		return (set(edges[0]) & set(edges[1])).pop()

	def findCenter_my(self, edges: list[list[int]]) -> int:

		starMap = {}
		count = len(edges)

		for edge in edges:
			x = edge[0]
			y = edge[1]

			if x in starMap:
				starMap[x] += 1
			else:
				starMap[x] = 1

			if y in starMap:
				starMap[y] += 1
			else:
				starMap[y] = 1

			if starMap[x] == count:
				return x

			if starMap[y] == count:
				return y

		return -1
