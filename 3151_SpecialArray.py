class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        N = len(nums)

        for i in range(N-1):
            if nums[i] % 2 == nums[i+1] % 2:
                return False
        return True
    

print(Solution().isArraySpecial([2,1,4]))
print(Solution().isArraySpecial([4,3,1,6]))