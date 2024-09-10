from functools import cache

class Solution:
    def findMaximumScore(self, nums: list[int]) -> int:
        N = len(nums)

        @cache
        def dp(idx):
            if idx == N-1:
                return 0
            
            res = 0
            for i in range(idx+1, N):
                temp = (i - idx) * nums[idx] + dp(i)
                res = max(temp, res)
            return res
        
        return dp(0)
    

    def findMaximumScore(self, nums: list[int]) -> int:
        N = len(nums)
        res = 0
        cur_max = nums[0]

        for i in range(1, N):
            res += cur_max
            cur_max = max(cur_max, nums[i])
        
        return res
        
print(Solution().findMaximumScore([1,3,1,5]))