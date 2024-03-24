from collections import defaultdict
import heapq
from math import ceil
from math import sqrt

class Solution:
    def minOperations(self, k: int) -> int:
        if k == 1:
            return 0
        ans = k
        for cur in range(1, k):
            op = (ceil(k / cur)-1) + (cur - 1)
            ans = min(ans, op)
        return ans
    
    def minOperations(self, k: int) -> int:
        cur = int(sqrt(k))
        if cur * cur == k:
            return 2 * cur - 2
        elif cur * (cur+1) >= k:
            return 2 * cur - 1
        
        return cur * 2
    
    def minOperations(self, k: int) -> int:
        cur = int(sqrt(k))
        return cur - 1 + ceil((k/cur) - 1)

    
print(Solution().minOperations(11))
print(Solution().minOperations(1))

