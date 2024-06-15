from collections import defaultdict
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        N = len(profits)
        capital_hq = []
        profit_hq = []
        res = w
        idx = 0

        for p, c in zip(profits, capital):
            if res >= c:
                heapq.heappush(profit_hq, (-p, c))
            else:
                heapq.heappush(capital_hq, (c, -p))
        
        while profit_hq and idx < k:
            cur_p, cur_c = heapq.heappop(profit_hq)
            res += (-1 * cur_p)

            while capital_hq and res >= capital_hq[0][0]:
                add_c, add_p = heapq.heappop(capital_hq)
                heapq.heappush(profit_hq, (add_p, add_c))
            idx += 1
        return res
    
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        N = len(profits)
        pro_list = []
        idx = 0
        res = w
        hq = []

        for c, p in zip(capital, profits):
            pro_list.append((c, p))
        
        pro_list.sort()

        for _ in range(k):
            while idx < N and pro_list[idx][0] <= res:
                heapq.heappush(hq, -pro_list[idx][1])
                idx += 1

            if len(hq) == 0:
                break
            res += -1 * heapq.heappop(hq)
        return res

        
print(Solution().findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))
print(Solution().findMaximizedCapital(3, 0, [3,2,1], [0,1,2]))
print(Solution().findMaximizedCapital(1, 2, [1,2,3], [1,1,2]))