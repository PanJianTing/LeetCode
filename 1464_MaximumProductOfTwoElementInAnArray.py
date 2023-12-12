class Solution:
    def maxProduct(self, nums) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
    
    def maxProduct(self, nums) -> int:
        max_num = 0
        second_num = 0

        for n in nums:
            if n > max_num:
                second_num = max_num
                max_num = n
            else:
                second_num = max(second_num, n)
        return (max_num - 1) * (second_num - 1)
    

print(Solution().maxProduct([3,4,5,2]))
print(Solution().maxProduct([1,5,4,5]))