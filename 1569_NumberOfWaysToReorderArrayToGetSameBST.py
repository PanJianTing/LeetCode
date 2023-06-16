import math

class Solution:
    def numOfWays(self, nums) -> int:
        M = len(nums)

        table = [[0] for _ in range(M) for _ in range(M)]
        for i in range(0, M):
            table[i][0] = table[i][i] = 1
        
        for i in range(2, M):
            for j in range(1, i):
                table[i][j] = table[i-1][j-1] + table[i-1][j]


        def dp(nums):
            N = len(nums)
            if N < 3:
                return 1
            leftNode = []
            rightNode = []
            for i in range(1, N):
                if nums[i] < nums[0]:
                    leftNode.append(nums[i])
                else:
                    rightNode.append(nums[i])
            return dp(leftNode) * dp(rightNode) * table[N - 1][len(leftNode)]
        
        return (dp(nums) - 1) % (10 ** 9 + 7)
    

    def numOfWays(self ,nums) -> int:

        def dp(nums):
            N = len(nums)
            if N < 3:
                return 1
            left = []
            right = []
            for i in range(1, N):
                if nums[i] < nums[0]:
                    left.append(nums[i])
                else:
                    right.append(nums[i])

            return dp(left) * dp(right) * math.comb(N, len(left))
        
        return dp(nums)