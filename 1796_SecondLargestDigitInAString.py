import heapq

class  Solution:
	def secondHighest(self, s: str) -> int:

		numberlist = []

		for c in s:
			if c.isnumeric() and c not in numberlist:
				if len(numberlist) < 2:
					heapq.heappush(numberlist, c)
				elif numberlist[0] < c:
					heapq.heapreplace(numberlist, c)


		if len(numberlist) > 1:
			return numberlist[0]

		return -1