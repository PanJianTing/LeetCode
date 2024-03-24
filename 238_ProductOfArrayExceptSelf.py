class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        N = len(nums)
        zero_cnt = 0
        zero_idx = 0
        total = 1
        ans = []

        for i, n in enumerate(nums):
            if n == 0:
                zero_cnt += 1
                zero_idx = i
            else:
                total *= n
        
        if zero_cnt >  1:
            return [0] * N
        elif zero_cnt == 1:
            ans = [0] * N
            ans[zero_idx] = total
            return ans
        for n in nums:
            ans.append(total//n)
        return ans
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        N = len(nums)
        L = [1] * N
        R = [1] * N
        res = [1] * N

        for i in range(1, N):
            L[i] = L[i-1] * nums[i-1]
        
        for i in range(N-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
        
        for i in range(N):
            res[i] = L[i] * R[i]
        return res
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        N = len(nums)
        res = [1] * N
        R = 1

        for i in range(1, N):
            res[i] = res[i-1] * nums[i-1]
        
        for i in range(N-2, -1, -1):
            R *= nums[i+1]
            res[i] *= R
        
        return res
    
print(Solution().productExceptSelf([1,2,3,4]))