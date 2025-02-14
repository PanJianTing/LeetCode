import heapq

class Solution:
    def makePrefSumNonNegative(self, nums: list[int]) -> int:
        hq = []
        cur = 0
        ans = 0

        for n in nums:
            cur += n
            if n < 0:
                heapq.heappush(hq, n)
            if cur < 0:
                cur -= heapq.heappop(hq)
                ans += 1

        return ans
    

print(Solution().makePrefSumNonNegative([6,-6,-3,3,1,5,-4,-3,-2,-3,4,-1,4,4,-2,6,0]))