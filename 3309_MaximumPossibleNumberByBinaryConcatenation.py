from functools import cmp_to_key

class Solution:
    def maxGoodNumber(self, nums: list[int]) -> int:
        bin_num_1 = bin(nums[0])[2:]
        bin_num_2 = bin(nums[1])[2:]        
        bin_num_3 = bin(nums[2])[2:]

        op1 = int(bin_num_1 + bin_num_2 + bin_num_3, 2)
        op2 = int(bin_num_1 + bin_num_3 + bin_num_2, 2)
        op3 = int(bin_num_2 + bin_num_1 + bin_num_3, 2)
        op4 = int(bin_num_2 + bin_num_3 + bin_num_1, 2)
        op5 = int(bin_num_3 + bin_num_1 + bin_num_2, 2)
        op6 = int(bin_num_3 + bin_num_2 + bin_num_1, 2)


        return max(op1, op2, op3, op4, op5, op6)
    

    def maxGoodNumber(self, nums: list[int]) -> int:
        
        def cmp(a, b):
            if a + b > b + a:
                return -1
            return 1
    
        nums = [bin(x)[2:] for x in nums]

        nums.sort(key=cmp_to_key(cmp))

        return int(''.join(nums), 2)
    
print(Solution().maxGoodNumber([1,2,3]))