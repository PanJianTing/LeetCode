class Solution:
    def search(self, nums, target) -> int:
        N = len(nums)
        
        l = 0
        r = N - 1
        

        def atS(st, now) -> bool:
            return nums[st] <= now

        def helper(st, now) -> bool:
            return nums[st] == now

        while l <= r:
            m = l + ((r-l) >> 1)

            if nums[m] == target:
                return True
            
            if helper(l, nums[m]):
                l += 1
                continue

            pivotArr  = atS(l, nums[m])
            targetArr = atS(l, target)

            if pivotArr ^ targetArr:

                if targetArr:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

        return False
    

    def search(self, nums, target) -> bool:
        N = len(nums)
        l = 0
        r = N - 1

        while l <= r:

            while l < r and nums[l] == nums[l+1]:
                l += 1
            
            while l < r and nums[r-1] == nums[r]:
                r -= 1
            
            m = r - ((r - l) >> 1)

            if nums[m] == target:
                return True

            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False




print(Solution().search([2,5,6,0,0,1,2], 0))                            # True
print(Solution().search([2,5,6,0,0,1,2], 3))                            # False
print(Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2))    # True
print(Solution().search([1], 0))                                        # False
print(Solution().search([3,1], 3))                                      # True
