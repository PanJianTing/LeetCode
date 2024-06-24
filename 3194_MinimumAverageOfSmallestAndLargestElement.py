class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        N = len(nums)
        nums.sort()
        l = 0
        r = N-1
        res = float('inf')

        while l < r:
            res = min(res, ((nums[r] + nums[l]) / 2))
            l += 1
            r -= 1
        
        return res
    
    
    
print(Solution().minimumAverage([7,8,3,4,15,13,4,1]))
print(Solution().minimumAverage([1,9,8,3,10,5]))
print(Solution().minimumAverage([1,2,3,7,8,9]))

