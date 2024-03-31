class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        N = len(nums)
        min_idx = -1
        max_idx = -1
        out = -1
        res = 0

        for i in range(N):
            cur = nums[i]

            if cur == minK:
                min_idx = i
            if cur == maxK:
                max_idx = i
            if cur < minK or cur > maxK:
                out = i

            res += max(0, min(min_idx, max_idx) - out)
        return res
    
print(Solution().countSubarrays([1,3,5,2,7,5], 1, 5))
print(Solution().countSubarrays([1,1,1,1], 1, 1))

        