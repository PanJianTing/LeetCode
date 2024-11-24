from collections import defaultdict

class Solution:
    def shareCandies(self, nums: list[int], k: int) -> int:
        N = len(nums)
        cnt_map = defaultdict(int)
        ans = 0

        for n in nums:
            cnt_map[n] += 1
        
        for i in range(N):
            cur = nums[i]
            cnt_map[cur] -= 1
            if cnt_map[cur] == 0:
                del cnt_map[cur]
            if i - k >= 0:
                cnt_map[nums[i-k]] += 1
            if i >= k-1:
                ans = max(ans, len(cnt_map))

        return ans
    
print(Solution().shareCandies([1,1,2,1], 2))