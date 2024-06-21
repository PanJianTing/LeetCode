class Solution:
    def maxSatisfied(self, customer: list[int], grumpy: list[int], minutes: int) -> int:
        N = len(customer)
        res = 0
        r = 0

        for c, g in zip(customer, grumpy):
            if g == 0:
                res += c
        l = 0
        r = l + minutes
        max_good = 0
        cur = 0

        for i in range(r):
            if grumpy[i] == 1:
                cur += customer[i]
                max_good = max(max_good, cur)
        
        for i in range(r, N):
            if grumpy[l] == 1:
                cur -= customer[l]
            if grumpy[i] == 1:
                cur += customer[i]
            l += 1
            max_good = max(max_good, cur)

        return res + max_good
    
    def maxSatisfied(self, customer: list[int], grumpy: list[int], minutes: int) -> int:
        N = len(customer)
        res = 0
        cur_max = 0

        for i in range(minutes):
            if grumpy[i] == 1:
                cur_max += customer[i]
            else:
                res += customer[i]
        
        temp_max = cur_max
        for i in range(minutes, N):
            if grumpy[i-minutes] == 1:
                temp_max -= customer[i-minutes]
            if grumpy[i] == 1:
                temp_max += customer[i]
            else:
                res += customer[i]
                
            cur_max = max(cur_max, temp_max)

        return res + cur_max

print(Solution().maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))
print(Solution().maxSatisfied([1], [0], 1))