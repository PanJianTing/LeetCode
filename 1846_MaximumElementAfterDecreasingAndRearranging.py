class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        
        N = len(arr)
        arr.sort()
        if arr[0] != 1:
            arr[0] = 1

        for i in range(1, N):
            if abs(arr[i] - arr[i-1]) > 1:
                arr[i] = arr[i-1] + 1
        
        return max(arr)
    
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        
        N = len(arr)
        arr.sort()
        cur = 1

        for i in range(1, N):
            if arr[i] > cur:
                cur += 1
        
        return cur
    
    def maximumElementAfterDecrementingAndRearranging(self, arr) -> int:
        N = len(arr)
        arr.sort()
        cur = 1

        for i in range(1, N):
            if arr[i] >= cur + 1:
                cur += 1
        
        return cur
    
    def maximumElementAfterDecrementingAndRearranging(self, arr) -> int:

        N = len(arr)
        count = [0] * (N+1)
        cur = 1

        for num in arr:
            count[min(num, N)] += 1

        for now in range(2, N+1):
            cur = min(cur + count[now], now)
        
        return cur

print(Solution().maximumElementAfterDecrementingAndRearranging([2,2,1,2,1]))
print(Solution().maximumElementAfterDecrementingAndRearranging([100,1,1000]))
print(Solution().maximumElementAfterDecrementingAndRearranging([1,2,3,4,5]))
