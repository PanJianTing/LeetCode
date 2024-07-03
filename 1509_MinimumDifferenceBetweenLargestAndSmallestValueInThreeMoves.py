import heapq

class Solution:
    def minDifference(self, nums: list[int]) -> int:
        N = len(nums)
        if N <= 4:
            return 0
        
        nums.sort()
        l = 0
        r = N-4
        res = nums[r] - nums[l]

        while r < N:
            res = min(res, nums[r] - nums[l])
            r += 1
            l += 1
        
        return res
    
    def minDifference(self, nums: list[int]) -> int:
        N = len(nums)
        if N <= 4:
            return 0
        res = float('inf')
        largest_nums = sorted(heapq.nlargest(4, nums))
        smallest_nums = sorted(heapq.nsmallest(4, nums))

        for i in range(4):
            res = min(res, largest_nums[i] - smallest_nums[i])

        return res
    

print(Solution().minDifference([1,5,0,10,14]))


