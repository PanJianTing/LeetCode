import heapq

class Solution:

    # Because the list contains negative number, so the two point approach isn't work well. 
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        N = len(nums)
        ans = float('inf')
        l = 0
        cur_sum = 0
        
        for i in range(N):
            cur_sum += nums[i]

            while l < i and cur_sum >= k:
                ans = min(ans, i - l + 1)
                cur_sum -= nums[l]
                l += 1
        

        return -1 if ans == float('inf') else ans
    
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        N = len(nums)
        ans = float('inf')
        prefix_hq = []
        cur_sum = 0

        for i in range(N):
            cur_sum += nums[i]

            if cur_sum >= k:
                ans = min(ans, i+1)
            
            while prefix_hq and cur_sum - prefix_hq[0][0] >= k:
                _, idx = heapq.heappop(prefix_hq)
                ans = min(ans, i - idx)
            
            heapq.heappush(prefix_hq, [cur_sum, i])
        
        return -1 if ans == float('inf') else ans


print(Solution().shortestSubarray([84,-37,32,40,95], 167))