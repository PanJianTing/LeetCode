from math import ceil
import heapq


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        ans = 0
        hq = []

        for n in nums:
            heapq.heappush(hq, -1 * n)

        for _ in range(k):
            cur = heapq.heappop(hq) * -1
            ans += cur

            heapq.heappush(hq, -1 * ceil(cur / 3))
        
        return ans
    
# print(Solution().maxKelements([10,10,10,10,10], 5))
print(Solution().maxKelements([1,10,3,3,3], 3))

