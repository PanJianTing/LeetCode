from functools import cache

class Solution:
    def maxEnergyBoost(self, A: list[int], B: list[int]) -> int:
        N = len(A)

        @cache
        def dp(cur, cur_A):
            if cur == N:
                return 0
            
            if cur_A:
                return max(A[cur] + dp(cur+1, True), dp(cur+1, False))
            else:
                return max(B[cur] + dp(cur+1, False), dp(cur+1, True))
                
        return max(dp(0, True), dp(0, False))
    
    def maxEnergyBoost(self, A: list[int], B: list[int]) -> int:
        N = len(A)
        preA = 0
        preB = 0
        curA = 0
        curB = 0

        for i in range(N):
            nextA = A[i] + max(curA, preB)
            nextB = B[i] + max(curB, preA)
            preA = curA
            preB = curB
            curA = nextA
            curB = nextB
        
        return max(curA, curB)
    
print(Solution().maxEnergyBoost([1,3,1], [3,1,1]))
print(Solution().maxEnergyBoost([4,1,1], [1,1,3]))
print(Solution().maxEnergyBoost([3,4,5], [6,6,4]))
print(Solution().maxEnergyBoost([4,6,4], [6,6,3]))

            