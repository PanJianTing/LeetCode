class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        N = len(nums)

        for i in range(1, N):
            if (nums[i] - nums[i-1]) > 1:
                return nums[i] - 1

        return N if nums[0] == 0 else 0
    
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        all_sum = ((0 + N) * (N + 1)) >> 1

        return all_sum - sum(nums)
    
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        all_nums = set([i for i in range(0, N+1)])

        return next(iter(all_nums - set(nums)))
    
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        
        for check in range(N+1):
            isFound = False
            for n in nums:
                if check == n:
                    isFound = True
                    break
            if isFound == False:
                return check
        return -1
    
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        cur_num_set = set(nums)
        
        for check in range(N+1):
            if check not in cur_num_set:
                return check
        
        return -1
    
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        ans = N

        for i in range(N):
            ans ^= i ^ nums[i]
        

        return ans
        
 
print(Solution().missingNumber([3,0,1]))
print(Solution().missingNumber([0,1]))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
print(Solution().missingNumber([1]))