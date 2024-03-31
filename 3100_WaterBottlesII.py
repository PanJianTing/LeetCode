class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExChanges: int) -> int:
        res = 0
        empty = numBottles
        res = numBottles

        while empty >= numExChanges:
            empty -= numExChanges
            numExChanges += 1
            res += 1
            empty += 1

        return res
    
print(Solution().maxBottlesDrunk(13, 6))
print(Solution().maxBottlesDrunk(10, 3))
            
