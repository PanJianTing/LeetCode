from math import ceil
from functools import cache

class Solution:
    def minArraySum(self, nums: list[int], k: int, op1: int, op2: int) -> int:
        N = len(nums)

        @cache
        def dp(idx, op1_cnt, op2_cnt):
            if idx == N:
                return 0

            if op1_cnt == 0 and op2_cnt == 0:
                return nums[idx] + dp(idx+1, 0, 0)

            no_op = nums[idx] + dp(idx+1, op1_cnt, op2_cnt)
            use_op1 = float('inf')
            use_op2 = float('inf')
            use_op2_op1 = float('inf')
            use_op1_op2 = float('inf')

            if op1_cnt > 0:
                use_op1 = ceil(nums[idx] / 2) + dp(idx+1, op1_cnt-1, op2_cnt)

            if op2_cnt > 0 and nums[idx] >= k:
                use_op2 = nums[idx] - k + dp(idx+1, op1_cnt, op2_cnt-1)
                if op1_cnt > 0:
                    use_op2_op1 = ceil((nums[idx] - k) / 2) + dp(idx+1, op1_cnt-1, op2_cnt-1)

            if op1_cnt > 0 and op2_cnt > 0 and ceil(nums[idx] / 2) >= k:
                use_op1_op2 = ceil(nums[idx] / 2) - k + dp(idx+1, op1_cnt-1, op2_cnt-1)

            return min(no_op, use_op1, use_op2, use_op2_op1, use_op1_op2)

        return dp(0, op1, op2)


print(Solution().minArraySum([2,8,3,19,3], 3, 1, 1))
            

            