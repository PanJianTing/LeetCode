from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        cnt_map = defaultdict(int)
        all_num = sorted(set(nums), reverse= True)
        
        for n in nums:
            cnt_map[n] += 1
        
        for n in all_num:
            if cnt_map[n] == 1:
                return n

        return -1
    
    def largestUniqueNumber(self, nums: list[int]) -> int:
        N = len(nums)

        if N == 1:
            return nums[0]

        nums.sort()
        idx = N-1

        while idx > -1:
            if idx == 0 or nums[idx] != nums[idx-1]:
                return nums[idx]
            while idx > 0 and nums[idx] == nums[idx-1]:
                idx -= 1
            idx -= 1
        return -1
    

    def largestUniqueNumber(self, nums: list[int]) -> int:
        N = len(nums)
        cnt_map = defaultdict(int)
        res = -1

        for n in nums:
            cnt_map[n] += 1

        for key in cnt_map.keys():
            if cnt_map[key] == 1:
                res = max(res, key)
        
        return res
    

    def largestUniqueNumber(self, nums: list[int]) -> int:
        N = len(nums)
        nums.sort(reverse=True)

        idx = 0
        while idx < N:
            if idx == N-1 or nums[idx] != nums[idx+1]:
                return nums[idx]
            while idx < N-1 and nums[idx] == nums[idx+1]:
                idx += 1
            idx += 1
        return -1

    
print(Solution().largestUniqueNumber([9,9,8,8]))
print(Solution().largestUniqueNumber([11,10,11]))
print(Solution().largestUniqueNumber([99]))
print(Solution().largestUniqueNumber([5,7,3,9,4,9,8,3,1]))