class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive_idx = 0
        negative_idx = 1
        ans = [0] * len(nums)

        for n in nums:
            if n > 0:
                ans[positive_idx] = n
                positive_idx += 2
            else:
                ans[negative_idx] = n
                negative_idx += 2
        return ans
    
print(Solution().rearrangeArray([3,1,-2,-5,2,-4]))
print(Solution().rearrangeArray([-1,1]))
