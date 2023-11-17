class Solution:
    def minPairSum(self, A) -> int:
        A.sort()
        N = len(A)
        ans = 0
        for i in range(0, N // 2):
            ans = max(ans, A[i] + A[N-i-1])

        return ans
    
    def minPairSum(self, A) -> int:
        A.sort()
        ans = 0
        l = 0
        r = len(A)-1

        while l < r:
            ans = max(ans, A[l] + A[r])
            l += 1
            r -= 1

        return ans
    
print(Solution().minPairSum([3,5,2,3]))
print(Solution().minPairSum([3,5,4,2,4,6]))
