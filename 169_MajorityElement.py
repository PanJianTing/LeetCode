from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        N = len(nums)
        cnt_map = defaultdict(int)

        for n in nums:
            cnt_map[n] += 1
        
        for n in cnt_map:
            if cnt_map[n] > (N >> 1):
                return n
        return 0
    
    def majorityElement(self, nums: list[int]) -> int:
        N = len(nums)
        thresh_hole = N >> 1

        for n in nums:
            cnt = 0
            for check in nums:
                if n == check:
                    cnt += 1

            if cnt > thresh_hole:
                return n
        return 0
    
    def majorityElement(self, nums: list[int]) -> int:
        N = len(nums)
        nums.sort()
        return nums[(N >> 1)]


print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))
print(Solution().majorityElement([6,5,5]))