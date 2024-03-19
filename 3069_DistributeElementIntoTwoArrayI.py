class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        N = len(nums)
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, N):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2
    
    def resultArray(self, nums: list[int]) -> list[int]:
        N = len(nums)
        p1 = 0
        p2 = 1
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, N):
            if nums[p1] > nums[p2]:
                arr1.append(nums[i])
                p1 = i
            else:
                arr2.append(nums[i])
                p2 = i

        return arr1 + arr2
    
print(Solution().resultArray([2,1,3]))
print(Solution().resultArray([5,4,3,8]))