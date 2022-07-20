class Solution:
    #要留之前相乘最大與相乘最小(因最小在 * ㄧ個負數 就是最大的了)
    def maxProduct(self, nums: list[int]) -> int:

        before_max = nums[0]
        before_min = nums[0]
        ans = max(nums)

        for i in range(1, len(nums)):
            num = nums[i]

            temp_max = max(num, before_max * num, before_min * num)
            before_min = min(num, before_max * num, before_min * num)

            before_max = temp_max


            ans = max(ans, before_max)

        return ans



# class Solution:
#     # time out
#     def maxProduct(self, nums: list[int]) -> int:

#         ans = max(nums)

#         now = 1

#         for i in range(0, len(nums)):
#             now = nums[i]
#             for j in range(i+1, len(nums)):
#                 now *= nums[j]
#                 if now > ans:
#                     ans = now
#         return ans




# Solution().maxProduct([2,3,-2,4])
Solution().maxProduct([-4,-3,-2])