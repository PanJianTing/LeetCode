class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:

        for i in range(0, len(nums)-2, 2):
            if nums[i] != nums[i+1]:
                return nums[i]

        return nums[-1]

    def singleNonDuplicate(self, nums: list[int]) -> int:

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (hi + lo) // 2
            halve_are_even = (hi - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if halve_are_even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if halve_are_even:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[hi]

    def singleNonDuplicate(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (hi + lo) // 2
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid+1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]

    def singleNonDuplicate(self, nums: list[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = left + (right - left) // 2

            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid] == nums[mid+1]):
                left = mid + 1
            else:
                right = mid
        return nums[left]


        
print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))
print(Solution().singleNonDuplicate([1, 1, 2]))


