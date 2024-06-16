class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        N = len(hours)
        res = 0

        for i in range(N):
            for j in range(i+1, N):
                if (hours[i] + hours[j]) % 24 == 0:
                    res += 1
            
        return res
    
print(Solution().countCompleteDayPairs([12,12,30,24,24]))
print(Solution().countCompleteDayPairs([72,48,24,3]))