class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        N = len(nums)
        nums.sort()
        
        ans = []
        idx = 0

        while idx < N:
            temp = []
            for _ in range(3):
                temp.append(nums[idx])
                idx += 1
            if temp[2] - temp[0] > k:
                return []
            ans.append(temp)

        return ans
    
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        N = len(nums)
        nums.sort()
        ans = []

        for i in range(0, N, 3):
            if nums[i+2] - nums[i] > k:
                return []

            ans.append([nums[i], nums[i+1], nums[i+2]])

        return ans 
    

print(Solution().divideArray([1,3,4,8,7,9,3,5,1], 2))
print(Solution().divideArray([17,15,20,16,15,10,20,19,17], 2))