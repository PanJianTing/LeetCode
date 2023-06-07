from functools import cache

class Solution:
    def probabilityOfHeads(self, A, target) -> float:        
        N = len(A)

        @cache
        def dp(idx, target):
            if target < 0:
                return 0
            
            if idx == N:
                if target == 0:
                    return 1
                else:
                    return 0
            
            return dp(idx + 1, target-1) * A[idx] + dp(idx + 1, target) * (1 - A[idx])
        
        return dp(0, target)