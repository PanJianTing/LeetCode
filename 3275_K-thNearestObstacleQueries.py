from collections import defaultdict, deque
import heapq

class Solution:
    def resultsArray(self, queries: list[list[int]], k: int) -> list[int]:
        N = len(queries)
        hq = []
        res = [-1] * N

        for i, (x, y) in enumerate(queries):
            heapq.heappush(hq, -1 * (abs(x) + abs(y)))

            while len(hq) > k:
                heapq.heappop(hq)

            if len(hq) >= k:
                res[i] = -1 * hq[0]
        
        return res
    
    def resultsArray(self, queries: list[list[int]], k: int) -> list[int]:
        hq = []
        res = []

        for x, y in queries:
            heapq.heappush(hq, -1 * (abs(x) + abs(y)))

            if len(hq) > k:
                heapq.heappop(hq)

            res.append(-1 * hq[0] if len(hq) == k else -1) 
        
        return res
     