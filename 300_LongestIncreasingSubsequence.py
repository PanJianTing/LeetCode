import bisect

class Solution:
    def lengthOfLIS(self, nums) -> int:
        N = len(nums)
        dp = [1] * N

        for i in range(N-1, -1, -1):
            cur = nums[i]
            temp = 0

            for j in range(i+1, N):
                if nums[j] > cur:
                    temp = max(temp, dp[j])
            dp[i] += temp        
        return max(dp)
    

    def lengthOfLIS(self, nums) -> int:
        N = len(nums)
        dp = [1] * N

        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
    

    def lengthOfLIS(self, nums) -> int:
        N = len(nums)
        sub = []
        sub.append(nums[0])

        for i in range(1, N):
            cur = nums[i]
            if cur > sub[-1]:
                sub.append(cur)
            else:
                j = bisect.bisect_left(sub, cur)
                j = 0
                while cur > sub[j]:
                    j += 1
                sub[j] = cur

        return len(sub)
    
    def lengthOfLIS(self, nums) -> int:
        N = len(nums)
        sub = []
        sub.append(nums[0])

        for i in range(1, N):
            cur = nums[i]
            if cur > sub[-1]:
                sub.append(cur)
            else:
                j = bisect.bisect_left(sub, cur)
                sub[j] = cur

        return len(sub)

                    
                    
            
    
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))
print(Solution().lengthOfLIS([3,4,5,1]))