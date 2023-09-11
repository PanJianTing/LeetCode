
from functools import cache

class Solution:
    def combinationSum4(self, nums, target):
        nums.sort()
        @cache
        def dp(remain):

            if remain == 0:
                return 1
            # if remain < 0:
            #     return 0
            ans = 0
            for n in nums:
                if n > remain:
                    break
                ans += dp(remain-n)
            
            return ans
        return dp(target)
    
    def combinationSum4(self, nums, target):
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i-n]

        return dp[target]



print(Solution().combinationSum4([1,2,3], 4))
print(Solution().combinationSum4([1,2,3], 3))
print(Solution().combinationSum4([1,2,3], 2))
print(Solution().combinationSum4([1,2,3], 1))
