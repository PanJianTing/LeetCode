from functools import lru_cache

class Solution:
    def PredictTheWinner(self, nums) -> bool:

        @lru_cache
        def maxDiff(left, right) -> int:
            if left == right:
                return nums[left]
            
            return max(nums[left] - maxDiff(left+1, right), nums[right] - maxDiff(left, right-1))
        
        return maxDiff(0, len(nums)-1) >= 0
    
    def PredictTheWinner(sefl, nums) -> bool:
        N = len(nums)

        dp = [[0] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = nums[i]

        for i in range(1, N):
            for left in range(0, N):
                right = left + i
                if right < N:
                    dp[left][right] = max(nums[left] - dp[left+1][right], nums[right] - dp[left][right-1])

        return dp[0][N-1] >= 0
    
    def PredictTheWinner(self, nums) -> bool:
        N = len(nums)
        dp = nums[:]
        
        for i in range(1, N):
            for left in range(0, N-i):
                right = left + i
                dp[left] = max(nums[left] - dp[left+1], nums[right] - dp[left])
            print(dp)

        return dp[0] >= 0

print(Solution().PredictTheWinner([1, 5, 2]))
print(Solution().PredictTheWinner([1, 5, 233, 7]))