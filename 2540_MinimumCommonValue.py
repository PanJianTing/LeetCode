class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        n1 = set(nums1)
        n2 = set(nums2)
        common = n1 & n2
        return min(common) if common else -1
    
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        p1 = 0
        p2 = 0
        N1 = len(nums1)
        N2 = len(nums2)

        while p1 < N1 and p2 < N2:
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            if nums1[p1] <= nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return -1
    
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        N1, N2 = len(nums1), len(nums2)
        if N1 < N2:
            return self.getCommon(nums2, nums1)
        
        def bs(target):
            l = 0
            r = len(nums2) - 1

            while l <= r:
                m = l + ((r-l) >> 1)
                if nums2[m] == target:
                    return True
                if nums2[m] < target:
                    l += 1
                else:
                    r -= 1
            return False
        
        for n in nums1:
            if bs(n):
                return n
        return -1




print(Solution().getCommon([1,2,3], [2,4]))
print(Solution().getCommon([1,2,3,6], [2,3,4,5]))