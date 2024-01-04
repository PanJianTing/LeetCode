from collections import defaultdict
from functools import cache
import math

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        cnt_map = defaultdict(int)
        all_num = set(nums)
        ans = 0

        for n in nums:
            cnt_map[n] += 1
        
        @cache
        def dp(n):
            if n == 0:
                return 0
            elif n == 1 or n < 0:
                return -1
            elif n == 2 or n == 3:
                return 1
            temp_2 = dp(n-2)
            temp_3 = dp(n-3)
            if temp_2 == -1:
                return 1 + temp_3
            elif temp_3 == -1:
                return 1 + temp_2
            return 1 + min(temp_2, temp_3)
        
        for n in all_num:
            if cnt_map[n] == 1:
                return -1
            ans += dp(cnt_map[n])
        return ans
    

    def minOperations(self, nums) -> int:
        cnt_map = defaultdict(int)
        all_num = set(nums)
        ans = 0

        for n in nums:
            cnt_map[n] += 1
        
        for n in all_num:
            cnt = cnt_map[n]
            if cnt == 1:
                return -1
            elif cnt % 3 == 2 or cnt % 3 == 1:
                ans += (cnt // 3) + 1
            elif cnt % 3 == 0:
                ans += (cnt // 3)
            # elif cnt % 2 == 0:
            #     ans += (cnt >> 1)
            else:
                return -1
            
        return ans
    
    def minOperations(self, nums) -> int:
        cnt_map = defaultdict(int)
        ans = 0

        for n in nums:
            cnt_map[n] += 1
        
        for cnt in cnt_map.values():
            if cnt == 1:
                return -1
            else:
                ans += math.ceil(cnt/3)
        
        return ans
    
    def minOperations(self, nums) -> int:
        cnt_map = defaultdict(int)

        for n in nums:
            cnt_map[n] += 1

        if 1 in cnt_map.values():
            return -1
        
        return sum(n // 3 + (n % 3 > 0) for n in cnt_map.values())
        
    

    
print(Solution().minOperations([2,3,3,2,2,4,2,3,4]))
print(Solution().minOperations([2,1,2,2,3,3]))
print(Solution().minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))
print(Solution().minOperations([152,152,152,152,152,152,152,152,152,152,152,152,215,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,114,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,215,152,152,152,152,152,152,152,152,114,152,152,152,152,152,114,152,152,152,114,152,152,152,114,152,152,152,114,152,152,152,152,152,215]))