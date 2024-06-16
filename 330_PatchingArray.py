class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        N = len(nums)
        res = 0
        idx = 0
        miss = 1

        while miss <= n:
            if idx < N and nums[idx] <= miss:
                miss += nums[idx]
                idx += 1
            else:
                miss = miss << 1
                res += 1
        return res
    
# print(Solution().minPatches([1,3], 6))
print(Solution().minPatches([1,5,10], 20))