class Solution:
    
    def missingElement(self, nums, k) -> int:
        N = len(nums)
        leak = 0

        for i in range(1, N):
            leak = nums[i] - nums[i-1] - 1
            if leak >= k:
                return nums[i-1] + k
            else:
                k -= leak

        return nums[-1] + k
    
    def missingElement(self, nums, k) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:
            m = r - ((r-l) >> 1)
            # m = l + ((r-l) >> 1)

            #   nums[m] - nums[0] - 1 - (m - 0 - 1) 
            # = nums[m] - nums[0] - 1 - m + 1 
            # = nums[m] - nums[0] - 1
            cnt = nums[m] - nums[0] - m

            if cnt >= k:
                r = m-1
            else:
                l = m

        # if nums[l] - nums[0] - l >= k:
        #     return nums[0] + k - l
        # else:
        #     return nums[0] + k + l
        # ans = nums[l] + k - (nums[l] - nums[0] - 1 - (l-0-1))
        #     = nums[l] + k - (nums[l] - nums[0] - 1 - l + 1)
        #     = nums[l] + k - (nums[l] - nums[0] - l)
        #     = nums[l] + k - nums[l] + nums[0] + l
        #     = k + nums[0] + l
        return nums[0] + k + l

    
print(Solution().missingElement([4,7,9,10], 1))     #5
print(Solution().missingElement([4,7,9,10], 3))     #8
print(Solution().missingElement([1,2,4], 3))        #6


print(Solution().missingElement([1,5,6,7,9,10,14,15,16,17,20,21,23], 5))        #11
    