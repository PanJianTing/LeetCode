from collections import defaultdict
from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        res = 0
        for v in range(k):
            dp = [0] * k
            for n in nums:
                dp[n % k] = max(dp[n % k], dp[(v-n) % k] + 1)
            res = max(res, max(dp))
        return res
    

    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for n in nums:
            remainder = n % k
            for j in range(k):
                dp[remainder][j] = max(dp[remainder][j], dp[j][remainder] + 1)
                res = max(res, dp[remainder][j])
        
        return res

# print(Solution().maximumLength([1,2,3,4,5], 2))
print(Solution().maximumLength([1,4,2,3,1,4], 3))