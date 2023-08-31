class Solution:
    def minimumReplacement(self, nums) -> int:
        # N = len(nums)
        ans = 0
        idx = 0

        while idx < len(nums)-1:

            if nums[idx] > nums[idx+1]:
                nums = nums[:idx] + [nums[idx-1], nums[idx] - nums[idx-1]] + nums[idx+1:]
                ans += 1
            
            idx += 1

        return ans
    
    def minimumReplacement(self, nums) -> int:
        ans = 0
        N = len(nums)

        for i in range(N-2, -1, -1):
            if nums[i] <= nums[i+1]:
                continue

            new_element = (nums[i] + nums[i+1] - 1) // nums[i+1]

            ans += new_element - 1

            nums[i] = nums[i] // new_element
        
        return ans
    
    def minimumReplacement(self, nums) -> int:
        ans = 0
        bound = nums[-1]
        N = len(nums)

        for i in range(N-2, -1, -1):
            a = nums[i]
            k = (a + bound - 1) // bound
            # if a % bound:
            #     k = a // bound + 1
            # else:
            #     k = a // bound

            bound = a // k
            ans += k - 1
        
        return ans
    
print(Solution().minimumReplacement([3, 9, 3]))
print(Solution().minimumReplacement([1, 2, 3, 4, 5]))
print(Solution().minimumReplacement([2, 1, 4, 6, 7, 3, 4]))
print(Solution().minimumReplacement([2,10,20,19,1]))