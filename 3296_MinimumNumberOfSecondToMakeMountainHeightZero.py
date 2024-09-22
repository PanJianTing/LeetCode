import heapq

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        N = len(workerTimes)
        res = 0
        hq = []

        for t in workerTimes:
            heapq.heappush(hq, (t, t, 1))
        
        for _ in range(mountainHeight):
            total_time, work_time, times = heapq.heappop(hq)
            res = max(total_time, res)
            heapq.heappush(hq, (total_time + work_time * (times + 1), work_time, times + 1))

        return res
    

print(Solution().minNumberOfSeconds(4, [2,1,1]))
print(Solution().minNumberOfSeconds(10, [3,2,2,4]))
print(Solution().minNumberOfSeconds(5, [1,5]))
print(Solution().minNumberOfSeconds(5, [1,7]))


