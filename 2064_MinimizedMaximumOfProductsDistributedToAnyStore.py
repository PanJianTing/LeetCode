import math
import heapq

class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        M = len(quantities)
        l = 0
        r = max(quantities)

        def check(cur):
            j = 0
            remaing = quantities[j]

            for i in range(n):
                if remaing <= cur:
                    j += 1
                    if j == M:
                        return True
                    else:
                        remaing = quantities[j]
                else:
                    remaing -= cur
            
            return False
        
        while l < r:
            m = l + ((r-l) >> 1)

            if check(m):
                r = m
            else:
                l = m + 1

        return l
    

    def minimizedMaximum(self, N: int, quantities: list[int]) -> int:

        hq = []

        for q in quantities:
            heapq.heappush(hq, (-q, q, 1))

        for _ in range(N-len(quantities)):

            _, cur_q, cur_store = heapq.heappop(hq)

            heapq.heappush(hq, (-cur_q / (cur_store+1), cur_q, cur_store + 1))
        
        _, cur_q, cur_store = heapq.heappop(hq)
        return math.ceil(cur_q / cur_store)

print(Solution().minimizedMaximum(6, [11,6])) 
print(Solution().minimizedMaximum(7, [15, 10, 10])) 
print(Solution().minimizedMaximum(1, [100000])) 
print(Solution().minimizedMaximum(26, [24,18,12,6,3,24,5,19,10,20,2,18,27,3,13,22,11,16,19,13])) 



