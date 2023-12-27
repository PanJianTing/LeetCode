from collections import defaultdict
from functools import cache
import heapq

class Solution:
    def minCost(self, c, time) -> int:
        N = len(c)
        ans = 0
        cur = 0
        
        for i in range(1, N):
            if c[cur] == c[i]:
                if time[cur] <= time[i]:
                    ans += time[cur]
                    cur = i
                else:
                    ans += time[i]
            else:
                cur = i
        return ans
    
    def minCost(self, c, time) -> int:
        N = len(c)
        max_cost = 0
        sum_cost = 0
        ans = 0
        
        for i in range(N):
            if i > 0 and c[i] != c[i-1]:
                ans += sum_cost - max_cost
                sum_cost = max_cost = 0
            sum_cost += time[i]
            max_cost = max(max_cost, time[i])
        ans += sum_cost - max_cost
        return ans
    
    def minCost(self, c, time) -> int:
        N = len(c)
        max_cost = 0
        ans = 0

        for i in range(N):
            if i > 0 and c[i] != c[i-1]:
                max_cost = 0
            ans += min(max_cost, time[i])
            max_cost = max(max_cost, time[i])
        return ans
    
    def minCost(self, c, time) -> int:
        N = len(c)
        ans = 0
        l = 0
        r = 0

        while l < N and r < N:
            cur_total = 0
            cur_max = 0

            while r < N and c[l] == c[r]:
                cur_total += time[r]
                cur_max = max(cur_max, time[r])
                r += 1
            ans += cur_total - cur_max
            l = r
        return ans
    
    def minCost(self, c, time) -> int:
        N = len(c)
        total_time = 0
        cur_max_time = 0

        for i in range(N):
            if i > 0 and c[i] != c[i-1]:
                cur_max_time = 0

            total_time += min(cur_max_time, time[i])
            cur_max_time = max(cur_max_time, time[i])
            
        return total_time


        
    
print(Solution().minCost("abaac", [1,2,3,4,5])) #3
print(Solution().minCost("abc", [1,2,3])) #0
print(Solution().minCost("aabaa", [1,2,3,4,1])) #2
print(Solution().minCost("aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1])) #26
