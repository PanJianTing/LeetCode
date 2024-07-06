class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur = 1
        direction = 1

        for t in range(time):
            cur += direction
            if cur == n:
                direction = -1
            if cur == 1:
                direction = 1
        
        return cur
    
    def passThePillow(self, n: int, time: int) -> int:
        interval = n-1
        times = time // interval
        remaining = time % interval
        if times & 1:
            return n - remaining
        return remaining + 1

print(Solution().passThePillow(4, 5))
print(Solution().passThePillow(3, 2))
