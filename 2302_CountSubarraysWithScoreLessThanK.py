from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        N = len(nums)
        prefix_sum = [0] * (N+1)
        res = 0
        l = 0

        for i in range(N):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        for r in range(1, N+1):
            
            while l < r and (r - l) * (prefix_sum[r] - prefix_sum[l]) >= k:
                l += 1
            res += (r-l)
        
        return res
    
    def countSubarrays(self, nums: list[int], k: int) -> int:
        N = len(nums)
        cur_sum = 0
        res = 0
        l = 0

        for r in range(N):
            cur_sum += nums[r]

            while l <= r and (r-l+1) * cur_sum >= k:
                cur_sum -= nums[l]
                l += 1
    
            res += (r - l + 1)
        
        return res
    

# print(Solution().countSubarrays([2,1,4,3,5], 10))
# print(Solution().countSubarrays([1,1,1], 5))
print(Solution().countSubarrays([9,5,3,8,4,7,2,7,4,5,4,9,1,4,8,10,8,10,4,7], 4))
