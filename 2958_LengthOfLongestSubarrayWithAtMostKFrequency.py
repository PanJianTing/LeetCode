from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        N = len(nums)
        cnt_map = defaultdict(int)
        l = 0
        res = 0

        for r in range(N):
            cnt_map[nums[r]] += 1
            while cnt_map.values() and max(cnt_map.values()) > k:
                cnt_map[nums[l]] -= 1
                l += 1
            res = max(res, r - l+1)
        return res
    
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        N = len(nums)
        cnt_map = defaultdict(int)
        l = 0
        res = 0

        for r in range(N):
            cnt_map[nums[r]] += 1
            while cnt_map[nums[r]] > k:
                cnt_map[nums[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
    
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        N = len(nums)
        cnt_map = defaultdict(int)
        st = 0
        charsWithOver = 0

        for end in range(N):
            cnt_map[nums[end]] += 1
            if cnt_map[nums[end]] == k+1:
                charsWithOver += 1
            
            if charsWithOver > 0:
                cnt_map[nums[st]] -= 1
                if cnt_map[nums[st]] == k:
                    charsWithOver -= 1
                st += 1
        return N - st
    
print(Solution().maxSubarrayLength([2,2,3], 1))
print(Solution().maxSubarrayLength([1,2,3,1,2,3,1,2], 2))
print(Solution().maxSubarrayLength([1,2,1,2,1,2,1,2], 1))
    