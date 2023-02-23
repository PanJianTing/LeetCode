class Solution:
    # time: O(n * log(n))
    def wiggleSort(self, nums: list[int]):

        nums.sort()

        for i in range(1, len(nums), 2):
            
            if i + 1 < len(nums):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        # print(nums)

        return

    def wiggleSort(self, nums: list[int]):

        for i in range(0, len(nums) - 1):
            if (i % 2) == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

            elif (i % 2) == 1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

        print(nums)
                
            

Solution().wiggleSort([3,5,2,1,6,4])
Solution().wiggleSort([6,6,5,6,3,8])