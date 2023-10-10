from functools import cache

class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:

        M = len(nums1)
        N = len(nums2)

        @cache
        def dp(i, j):
            if i == M or j == N:
                return 0
            
            allUse = dp(i+1, j+1) + nums1[i] * nums2[j]
            return max(allUse, dp(i+1, j), dp(i, j+1))
        
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        elif min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        return dp(0, 0)


    def maxDotProduct(self, nums1, nums2) -> int:

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        elif min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        M = len(nums1)
        N = len(nums2)

        dp = [[0] * (N + 1) for _ in range(M+1)]

        for i in range(1, M+1):
            for j in range(1, N+1):
                dp[i][j] = max(nums1[i-1] * nums2[j-1] + dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        return dp[M][N]
       
print(Solution().maxDotProduct([2, 1, -2, 5], [3, 0, -6]))
print(Solution().maxDotProduct([3, -2], [2, -6, 7]))
print(Solution().maxDotProduct([-1, -1], [1, 1]))