class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        N = len(arr)
        r = N-1

        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1

        ans = r
        l = 0

        while l < r and (l == 0 or arr[l-1] <= arr[l]):

            while r < N and arr[l] > arr[r]:
                r += 1
            ans = min(ans, r - l - 1)
            l += 1
        
        return ans
    
print(Solution().findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))
        
        