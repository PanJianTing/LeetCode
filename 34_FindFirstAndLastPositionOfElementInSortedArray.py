class Solution:
    def searchRange(self, nums, target) -> list[int]:
        st = -1
        end = -1

        for i, n in enumerate(nums):

            if target == n:
                if st == -1:
                    st = i
                end = i
        return [st, end]
    
    def searchRange(self, nums, target) -> list[int]:

        if nums == []:
            return [-1, -1]

        l = 0
        r = len(nums) - 1

        st = -1

        while l < r:
            m = l + ((r-l) >> 1)

            if nums[m] < target:
                l = m+1
            else:
                r = m

        if nums[l] != target:
            return [-1, -1]
        else:
            st = l
        

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r-l) >> 1)

            if nums[m] <= target:
                l = m+1
            else:
                r = m-1

        return [st, r]

        
print(Solution().searchRange([5,7,7,8,8,10], 8))
print(Solution().searchRange([5,7,7,8,8,10], 6))
print(Solution().searchRange([5,7,8,8,10], 7))
print(Solution().searchRange([1], 1))

# print(Solution().searchRange([], 0))


