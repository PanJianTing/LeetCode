class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        M = len(nums1)
        N = len(nums2)

        i = 0
        j = 0
        newArray = []

        while i < M and j < N:
            if nums1[i] < nums2[j]:
                newArray.append(nums1[i])
                i += 1
            else:
                newArray.append(nums2[j])
                j += 1

        if i < M:
            newArray.extend(nums1[i:])
        else:
            newArray.extend(nums2[j:])


        totalL = len(newArray)
        m = totalL >> 1

        if totalL % 2 == 0:
            
            return (newArray[m-1] + newArray[m]) / 2

        return newArray[m]
    
    def findMedianSortedArrays(self, nums1, nums2):
        M = len(nums1)
        N = len(nums2)
        needCnt = (M + N) >> 1
        i = 0
        j = 0

        def getCnt():
            nonlocal i, j
            ans = 0
            if i < M and j < N:
                if nums1[i] < nums2[j]:
                    ans = nums1[i]
                    i += 1
                else:
                    ans = nums2[j]
                    j += 1
            elif i < M:
                ans = nums1[i]
                i += 1
            else:
                ans = nums2[j]
                j += 1
            return ans
            
        if (M+N) % 2:
            for _ in range(needCnt):
                _ = getCnt()
            return getCnt()
        else:
            for _ in range(needCnt-1):
                _ = getCnt()
            return (getCnt() + getCnt()) / 2


    def findMedianSortedArrays(self, A, B):
        M = len(A)
        N = len(B)
        half = (M+N) >> 1

        def dp(k, a_start, a_end, b_start, b_end):
            if a_start > a_end:
                return B[k - a_start]
            if b_start > b_end:
                return A[k - b_start]
            
            a_mid = a_start + ((a_end - a_start) >> 1)
            b_mid = b_start + ((b_end - b_start) >> 1)

            a_val = A[a_mid]
            b_val = B[b_mid]

            if a_mid + b_mid < k:
                if a_val <= b_val:
                    return dp(k, a_mid+1, a_end, b_start, b_end)
                else:
                    return dp(k, a_start, a_end, b_mid + 1, b_end)
            else:
                if a_val <= b_val:
                    return dp(k, a_start, a_end, b_start, b_mid - 1)
                else:
                    return dp(k, a_start, a_mid-1, b_start, b_end)
                
        if (M+N) % 2 == 1:
            return dp(half, 0, M-1, 0, N-1)
        else:
            return (dp(half, 0, M-1, 0, N-1) + dp(half-1, 0, M-1, 0, N-1)) / 2
        
    def findMedianSortedArrays(self, A, B):
        if len(A) > len(B):
            A, B = B, A
        
        minimize = float('-inf')
        maximize = float('inf')
        M = len(A)
        N = len(B)
        l = 0
        r = M

        while l <= r:
            a_idx = l + ((r-l) >> 1)
            b_idx = ((M + N + 1) >> 1) - a_idx

            a_left = minimize if a_idx - 1 < 0 else A[a_idx-1]
            a_right = maximize if a_idx >= M else A[a_idx]
            b_left = minimize if b_idx - 1 < 0 else B[b_idx-1]
            b_right = maximize if b_idx >= N else B[b_idx]

            if a_left <= b_right and a_right >= b_left:
                if (M+N) % 2:
                    return max(a_left, b_left)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            if a_left > b_right:
                r = a_idx - 1
            else:
                l = a_idx + 1
        


print(Solution().findMedianSortedArrays([1,3], [2]))        
print(Solution().findMedianSortedArrays([1,3], [2,4]))
print(Solution().findMedianSortedArrays([], [2]))