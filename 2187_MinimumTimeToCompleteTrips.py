class Solution:
    # if minimum time is t, bus count is n, the time complexity O(t * n)
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        
        endTrip = 0
        ans = 0
        while endTrip < totalTrips:

            nowTrip = 0
            ans += 1
            for busTime in time:
                nowTrip += ans // busTime

            endTrip = nowTrip
        
        return ans
    
    def minimumTime(self, time: list[int], totalTrips: int) -> int:

        maxTime = min(time) * totalTrips
        minTime = 0

        while minTime < maxTime:
            nowTime = minTime + ((maxTime - minTime) >> 1)

            nowTrip = 0
            for busTime in time:
                nowTrip += nowTime // busTime

            if nowTrip < totalTrips:
                minTime = nowTime + 1
            else:
                maxTime = nowTime

        return minTime

        

print(Solution().minimumTime([1,2,3], 5))
print(Solution().minimumTime([2], 1))