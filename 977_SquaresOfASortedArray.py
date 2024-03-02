class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        N = len(nums)
        for i in range(N):
            nums[i] *= nums[i]

        return sorted(nums)
    
    def sortedSquares(self, nums: list[int]) -> list[int]:
        N = len(nums)
        squares = [0] * N
        left = 0
        right = N-1

        for i in range(N-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                squares[i] = nums[right] * nums[right]
                right -= 1
            else:
                squares[i] = nums[left] * nums[left]
                left += 1
        return squares

    
    
print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-7,-3,2,3,11]))