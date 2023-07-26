import math

class Solution:

    def allTime(self, cnt, dist, speed) -> float:
        time = 0.0

        for i in range(cnt):
            t = dist[i] / speed
            if i == cnt - 1:
                time += t
            else:
                time += math.ceil(t)
        
        return time


    def minSpeedOnTime(self, dist, hour) -> int:
        if hour <= len(dist)-1:
            return -1
            
        cnt = len(dist)
        left = 1
        right = int(max(dist) + dist[-1]/(hour - cnt + 1)) + 1

        minTime = -1
        

        while left <= right:
            mid = left + ((right - left) >> 1)

            if self.allTime(cnt, dist, mid) <= hour:
                minTime = mid
                right = mid - 1
            else:
                left = mid + 1

        return minTime
    
# print(Solution().minSpeedOnTime([1,3,2], 6))
# print(Solution().minSpeedOnTime([1,3,2], 2.7))
# print(Solution().minSpeedOnTime([1,3,2], 1.9))
# print(Solution().minSpeedOnTime([5,3,4,6,2,2,7], 10.92))
print(Solution().minSpeedOnTime([1,1, 10000000], 2.1))