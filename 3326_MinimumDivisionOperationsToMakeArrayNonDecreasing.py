class Solution:
    def minOperations(self, nums: list[int]) -> int:
        N = len(nums)
        ans = 0
        
        def findNum(n1, n2):
            for i in range(2, n1+1):
                if n2 % i == 0:
                    return i
            return -1


        for i in range(N-2, -1, -1):
            if nums[i] > nums[i+1]:
                new_num = findNum(nums[i+1], nums[i])
                if new_num == -1:
                    return -1
                nums[i] = new_num
                ans += 1
        return ans
    
print(Solution().minOperations([25, 7]))
print(Solution().minOperations([7,7,6]))
print(Solution().minOperations([1,1,1,1]))
