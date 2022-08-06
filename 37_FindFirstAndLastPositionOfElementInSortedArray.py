

# class Solution:
#     def searchRange(self, nums: list[int], target: int) -> list[int]:

#         firstIndex = -1
#         lastIndex = -1

#         for index in range(0, len(nums)):
#             if nums[index] == target:
#                 firstIndex = index
#                 break
        
#         for index in range(len(nums)-1 , -1, -1):
#             if nums[index] == target:
#                 lastIndex = index
#                 break

#         # print([firstIndex, lastIndex])

#         return [firstIndex, lastIndex]

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        firstIndex = self.findBound(nums, target, True)
        if firstIndex == -1:
            return [-1, -1]
        lastIndex = self.findBound(nums, target, False)

        print([firstIndex, lastIndex])
        return [firstIndex, lastIndex]


    def findBound(self, nums:list[int], target: int, isFirst: bool) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:
            index = (left+right) // 2

            if nums[index] == target:
                if isFirst:
                    if index == 0 or nums[index - 1] != target:
                        return index
                    right = index - 1
                else:
                    if index == len(nums) - 1 or nums[index + 1] != target:
                        return index
                    left = index + 1
                
            elif nums[index] < target:
                left = index+1
            else:
                right = index-1

        return -1




Solution().searchRange([5,7,7,8,8,10], 8)
