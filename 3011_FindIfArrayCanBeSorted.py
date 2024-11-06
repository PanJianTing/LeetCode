class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        N = len(nums)

        for i in range(N):
            for j in range(N-i-1):
                if nums[j] <= nums[j+1]:
                    continue
                else:
                    if bin(nums[j]).count('1') == bin(nums[j+1]).count('1'):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                    else:
                        return False
        
        return True
    

    def canSortArray(self, nums: list[int]) -> bool:
        N = len(nums)
        cur_bit_count = bin(nums[0]).count('1')
        max_num = nums[0]
        min_num = nums[0]

        pre_max_num = float('-inf')

        for i in range(1, N):
            if cur_bit_count == bin(nums[i]).count('1'):
                max_num = max(max_num, nums[i])
                min_num = min(min_num, nums[i])
            else:
                if min_num < pre_max_num:
                    return False
                
                pre_max_num = max_num
                max_num = nums[i]
                min_num = nums[i]
                cur_bit_count = bin(nums[i]).count('1')
        
        return False if min_num < pre_max_num else True
    

    def canSortArray(self, nums: list[int]) -> bool:
        N = len(nums)

        for i in range(0, N-1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                if bin(nums[i]).count('1') == bin(nums[i+1]).count('1'):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                else:
                    return False
                
        for i in range(N-1, 0, -1):
            if nums[i] >= nums[i-1]:
                continue
            else:
                if bin(nums[i]).count('1') == bin(nums[i-1]).count('1'):
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                else:
                    return False
                
        return True

        
    
print(Solution().canSortArray([8,4,2,9,5]))
print(Solution().canSortArray([8,4,2,30,15]))
print(Solution().canSortArray([1,2,3,4,5]))
print(Solution().canSortArray([3,16,8,4,2]))