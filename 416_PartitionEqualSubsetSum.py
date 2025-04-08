from functools import cache

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        N = len(nums)
        all_sum = sum(nums)

        if all_sum & 1:
            return False
        target_sum = (all_sum >> 1)

        @cache
        def dfs(cur_idx, cur_sum):
            if cur_sum == 0:
                return True
            if cur_idx == N or cur_sum < 0:
                return False

            return dfs(cur_idx + 1, cur_sum - nums[cur_idx]) or dfs(cur_idx + 1, cur_sum)

        return dfs(0, target_sum)
    

    def canPartition(self, nums: list[int]) -> bool:
        N = len(nums)
        all_sum = sum(nums)

        if all_sum & 1:
            return False
        target_sum = all_sum >> 1
        dp = [[False] * (target_sum + 1) for _ in range(N+1)]
        dp[0][0] = True

        for i in range(1, N+1):
            cur = nums[i-1]
            for j in range(target_sum+1):
                if j < cur:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-cur]
        
        return dp[N][target_sum]
    
    def canPartdition(self, nums: list[int]) -> bool:
        N = len(nums)
        all_sum = sum(nums)

        if all_sum & 1:
            return False
        target_sum = all_sum >> 1
        dp = [False] * (target_sum + 1)
        dp[0] = True

        for i in range(0, N):
            cur = nums[i]
            for j in range(target_sum, cur-1, -1):
                dp[j] |=  dp[j-cur]
        
        return dp[target_sum]
    



# print(Solution().canPartition([1,2,3,5]))
# print(Solution().canPartition([1,5,11,5]))
# print(Solution().canPartition([2,2,1,1]))
print(Solution().canPartition([3,4,2,1]))