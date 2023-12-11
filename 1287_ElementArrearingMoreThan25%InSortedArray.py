import bisect


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:

        countMap = {}

        overCount = len(arr) // 4
        result = 0

        for count in arr:
            if count in countMap:
                countMap[count] += 1
            else:
                countMap[count] = 1
        
        for count in countMap.keys():
            if countMap[count] > overCount and count > result:
                result = count
        return result
    
    def findSpecialInteger(self, arr: list[int]) -> int:
        overCount = len(arr) // 4

        for i in range(len(arr)):
            if arr[i] == arr[i+overCount]:
                return arr[i]

        return 0
    
    def findSpecialInteger(self, arr: list[int]) -> int:
        N = len(arr)
        size = len(arr) >> 2

        for i in range(0, N-size):
            if arr[i] == arr[i+size]:
                return arr[i]
            
    
    def bs_left(self, A, target) -> int:
        l = 0
        r = len(A) - 1

        while l <= r:
            m = l + ((r-l) >> 1)

            if A[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
    
    def bs_right(self, A, target) -> int:
        l = 0
        r = len(A) - 1

        while l <= r:
            m = l + ((r-l) >> 1)
            if A[m] <= target:
                l = m + 1
            else:
                r = m - 1
        return l
    
    def findSpecialInteger(self, arr) -> int:
        N = len(arr)
        target_cnt = N >> 2
        candidates = [arr[N >> 2], arr[N >> 1], arr[(3*N) >> 2]]

        for can in candidates:
            # left = bisect.bisect_left(arr, can)
            # right = bisect.bisect_right(arr, can) - 1

            left = self.bs_left(arr, can)
            right = self.bs_right(arr, can) - 1

            # print(can, left, right)
            if right - left + 1 > target_cnt:
                return can
            
        

print(Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10]))
print(Solution().findSpecialInteger([1, 1]))
print(Solution().findSpecialInteger([1]))