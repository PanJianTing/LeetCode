from functools import lru_cache
from collections import defaultdict

class Solution:

    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:

        m = len(nums1)
        n = len(nums2)

        @lru_cache
        def dp(idx1: int, idx2: int) -> int:

            ans = 0
            if (idx1 < m) == False:
                return ans
            target = nums1[idx1]

            for i in range(idx2, n):
                if nums2[i] == target:
                   ans = max(ans, 1 + dp(idx1 + 1, i+1))
                else:
                    ans = max(ans, dp(idx1, i+1))
            return ans
        
        return dp(0, 0)
    
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        dp = defaultdict(int)
        m = len(nums1)
        n = len(nums2)

        for i in range(0, m):
            for j in range(0, n):
                dp[i,j] = max(dp[i-1, j-1] + (nums1[i] == nums2[j]), dp[i-1, j], dp[i, j-1])
        return dp[m-1, n-1]
    
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:

        m = len(nums1)
        n = len(nums2)

        @lru_cache
        def dp(idx1: int, idx2: int) -> int:
            if idx1 <= 0 or idx2 <= 0:
                return 0
            if nums1[idx1 - 1] == nums2[idx2 - 1]:
                return 1 + dp(idx1-1, idx2-1)
            else:
                return max(dp(idx1-1, idx2), dp(idx1, idx2 - 1))
        
        return dp(m, n)
    
print(Solution().maxUncrossedLines([1,4,2], [1,2,4]))
print(Solution().maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))

