import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        l = 1
        r = max(piles)

        while l < r:
            m = l + ((r - l) >> 1)

            t = 0

            for c in piles:
                t += (c - 1) // m + 1
                # t += math.ceil(c / m)
                # t += c // m
                # if c % m > 0:
                #     t += 1
            
            if t > h:
                l = m + 1
            else:
                r = m

        return l
    

print(Solution().minEatingSpeed([3,6,7,11], 8))
print(Solution().minEatingSpeed([30,11,23,4,20], 5))
print(Solution().minEatingSpeed([30,11,23,4,20], 6))