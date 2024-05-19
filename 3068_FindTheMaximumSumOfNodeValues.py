from functools import cache

class Solution:

    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        N = len(nums)

        @cache
        def dp(idx, isEven):
            if idx == N:
                if isEven:
                    return 0
                else:
                    return float('-inf')
            noXOR = nums[idx] + dp(idx+1, isEven)
            xor = (nums[idx] ^ k) + dp(idx+1, (not isEven))

            return max(noXOR, xor)
        return dp(0, 1)


    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        N = len(nums)
        dp = [[-1] * 2 for _ in range(N)]

        def maxSumOfNodes(idx, isEven):

            if idx == N:
                if isEven:
                    return 0
                else:
                    return float('-inf')
            
            if dp[idx][isEven] != -1:
                return dp[idx][isEven]
            
            noXor = nums[idx] + maxSumOfNodes(idx+1, isEven)
            xor = (nums[idx] ^ k) + maxSumOfNodes(idx+1, (isEven ^ 1))

            dp[idx][isEven] = max(noXor, xor)
            return dp[idx][isEven]
        
        return maxSumOfNodes(0, 1)
    
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        N = len(nums)
        dp = [[-1] * 2 for _ in range(N+1)]

        dp[N][0] = float('-inf')
        dp[N][1] = 0

        for idx in range(N-1, -1, -1):
            for isEven in range(2):
                noXor = nums[idx] + dp[idx+1][isEven]
                xor = (nums[idx] ^ k) + dp[idx+1][(not isEven)]

                dp[idx][isEven] = max(noXor, xor)
        return dp[0][1]
    
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        N = len(nums)
        netChanges = [0] * N

        res = sum(nums)

        for i in range(N):
            netChanges[i] = (nums[i] ^ k) - nums[i]
        
        netChanges = sorted(netChanges, reverse= True)

        for i in range(0, N, 2):
            if i+1 < N and netChanges[i] + netChanges[i+1] > 0:
                res += (netChanges[i] + netChanges[i+1])
            else:
                break
        return res
    
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        N = len(nums)
        positive_min = float('inf')
        negative_max = float('-inf')
        res = 0
        cnt = 0

        for i in range(N):
            res += nums[i]
            netChange = (nums[i] ^ k) - nums[i]

            if netChange > 0:
                positive_min = min(positive_min, netChange)
                res += netChange
                cnt += 1
            else:
                negative_max = max(negative_max, netChange)

        if cnt % 2 == 0:
            return res
        
        return max(res - positive_min, res + negative_max)
                

    
print(Solution().maximumValueSum([1,2,1], 3, [[0,1],[0,2]]))
        

