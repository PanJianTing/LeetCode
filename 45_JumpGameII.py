class Solution:

    # O(n)
    def jump(self, nums: list[int]) -> int:

        ans = 0
        n = len(nums)
        
        curr_end = curr_far = 0

        for i in range(0, n-1):
            curr_far = max(curr_far, i + nums[i])

            if i == curr_end:
                ans += 1
                curr_end = curr_far

        return ans

    # O(n^2)
    def jump(self, nums: list[int]) -> int:
        stepList = [999999] * len(nums)
        stepList[0] = 0

        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] + j >= i:
                    stepList[i] = min(stepList[i], stepList[j] + 1)

        return stepList[len(nums) - 1]

print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([2,3,0,1,4]))
print(Solution().jump([1,2,1,1,1]))