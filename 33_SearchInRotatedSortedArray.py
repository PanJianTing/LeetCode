class Solution:

    def search(self, nums, target) -> int:

        N = len(nums)

        for i in range(0, N):
            if target == nums[i]:
                return i

        return -1
    
    def search(self, nums, target) -> int:
        N = len(nums)
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = r - ((r - l) >> 1)

            if m+1 >= N:
                l = m
            else:
                if nums[m] > nums[m+1] and nums[m] > nums[m-1]:
                    break
                elif nums[m] < nums[m+1]:
                    l = m
                else:
                    r = m - 1
        
        print(l)

Solution().search([5,6,7,0,1,2,4], 0)