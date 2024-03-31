class Solution:
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        N = len(nums)
        cur = 1
        res = 1

        for i in range(1, N):
            if nums[i] == nums[i-1]:
                cur = 1
            else:
                cur += 1
            res += cur

        return res
    
print(Solution().countAlternatingSubarrays([0,1,1,1]))
print(Solution().countAlternatingSubarrays([1,0,1,0]))
print(Solution().countAlternatingSubarrays([0,0,1,0]))

        