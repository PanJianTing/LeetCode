class Solution:

    def peakIndexInMountainArray(self, arr) -> int:
        i = 0

        while arr[i] < arr[i+1]:
            i += 1

        return i

    def peakIndexInMountainArray(self, arr) -> int:
        
        l = 0
        r = len(arr) - 1

        while l < r:
            mid = l + ((r - l) >> 1)
            
            if mid == 0:
                l = mid + 1
                continue
            
            if mid == (len(arr) - 1):
                r = mid - 1
                continue

            if arr[mid-1] < arr[mid] < arr[mid+1]:
                l = mid+1
                continue
            
            if arr[mid-1] > arr[mid] > arr[mid+1]:
                r = mid - 1
                continue

            return mid
        
        return l
    

    def peakIndexInMountainArray(self, arr) -> int:
        l = 0
        r = len(arr)

        while l < r:
            mid = l + ((r-l) >> 1)
            # mid = (l + r) >> 1

            if arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l
    
    # Golden Section

    def peakIndexInMountainArray(self, A) -> int:
        def gold1(l, r):
            return l + int(round((r-l) * 0.382))
        
        def gold2(l, r):
            return l + int(round((r-l) * 0.618))
        
        l = 0
        r = len(A) - 1
        x1 = gold1(l, r)
        x2 = gold2(l, r)
        while x1 < x2:
            if A[x1] < A[x2]:
                l = x1
                x1 = x2
                x2 = gold1(x1, r)
            else:
                r = x2
                x2 = x1
                x1 = gold2(l, x2)
        
        return A.index(max(A[l: r + 1]), l)

    
print(Solution().peakIndexInMountainArray([0,1,0]))
print(Solution().peakIndexInMountainArray([0,2,1,0]))
print(Solution().peakIndexInMountainArray([0,10,5,2]))
print(Solution().peakIndexInMountainArray([18,29,38,59,98,100,99,98,90]))
print(Solution().peakIndexInMountainArray([3,9,8,6,4]))