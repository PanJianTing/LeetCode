class Solution:
	def constructRectangle(self, area: int) -> list[int]:
		length = int(area**.5)

		for i in range(length, -1, -1):
			if area % i == 0:
				break
		return [i , area // i]

	def constructRectangle_my(self, area: int) -> list[int]:


		L = area
		W = 1

		while W < L:
			if area % (W) == 0:
				L = area//(W)

			W += 1

		return [L, area//L]