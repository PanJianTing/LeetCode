class Solution:
    
    def minSubArrayLen(self, s, nums) -> int:
        N = len(nums)
        i = 0
        res = N + 1

        for j in range(0, N):
            s -= nums[j]
            while s <= 0:
                res = min(res, j-i+1)
                s += nums[i]
                i += 1
        return res % (N+1)
    
    def minSubArrayLen(self, s, nums) -> int:
        N = len(nums)
        ans = (N+1)
        left = 0
        nowSum = 0

        for right in range(0, N):
            nowSum += nums[right]

            while nowSum >= s:
                ans = min(ans, right - left + 1)
                nowSum -= nums[left]
                left += 1
        return ans % (N+1)
    
# print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
# print(Solution().minSubArrayLen(4, [1,4,4]))
print(Solution().minSubArrayLen(11, [1,2,3,4,5]))