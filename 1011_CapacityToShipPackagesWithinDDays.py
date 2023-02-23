class Solution:
    def feasible(self, weights: list[int], c: int, days: int) -> bool:
        daysNeeded = 1
        currentLoad = 0

        for weight in weights:
            currentLoad += weight
            if currentLoad > c:
                daysNeeded += 1
                currentLoad = weight
        
        return daysNeeded <= days
    
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l + r) // 2
            if self.feasible(weights, mid, days):
                r = mid
            else:
                l = mid + 1

        return r

print(Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))


