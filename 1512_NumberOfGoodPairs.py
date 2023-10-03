from collections import defaultdict
from typing import List

class Solution:
    def numIdenticalPairs(self, nums) -> int:
        ans = 0
        N = len(nums)
        for i in range(0, N):
            for j in range(i+1, N):
                if nums[i] == nums[j]:
                    ans += 1
        return ans
    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        numMap = defaultdict(int)

        for n in nums:
            numMap[n] += 1
        
        for v in numMap.values():
            if v > 1:
                cnt = v - 1
                ans += ((cnt + 1) * cnt) >> 1
        
        return ans
    
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ans = 0
        cur_cnt_map = {}

        for n in nums:
            if n in cur_cnt_map:
                cur_cnt_map[n] += 1
                ans += cur_cnt_map[n]
            else:
                cur_cnt_map[n] = 0
        
        return ans
    
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ans = 0
        cur_cnt_map = defaultdict(int)

        for n in nums:
            ans += cur_cnt_map[n]
            cur_cnt_map[n] += 1
        
        return ans
    
print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
print(Solution().numIdenticalPairs([1,1,1,1]))
print(Solution().numIdenticalPairs([1,2,3]))