from collections import defaultdict
import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        N = len(nums)
        res = [0] * N
        hq = []
        
        for i, n in enumerate(nums):
            heapq.heappush(hq, (n, i))
        
        idx = 0
        while idx < k:
            cur_n, cur_idx = heapq.heappop(hq)
            cur_n *= multiplier
            heapq.heappush(hq, (cur_n, cur_idx))
            idx += 1
        
        while hq:
            cur_n, cur_idx = heapq.heappop(hq)
            res[cur_idx] = cur_n
        
        return res
        
        
        