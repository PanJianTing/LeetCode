class Solution:
    def maximumTotalCost(self, nums: list[int]) -> int:
        N = len(nums)
        addRes = nums[0]
        subRes = nums[0]

        for i in range(1, N):
            tempAdd = max(addRes, subRes) + nums[i]
            tempSub = addRes - nums[i]

            addRes = tempAdd
            subRes = tempSub
        
        return max(addRes, subRes)

print(Solution().maximumTotalCost([1,-2,3,4]))
print(Solution().maximumTotalCost([1,-1,1,-1]))
