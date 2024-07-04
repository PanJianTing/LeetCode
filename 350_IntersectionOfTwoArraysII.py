from collections import defaultdict

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        p1 = 0
        p2 = 0
        nums1.sort()
        nums2.sort()
        res = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
        return res
    
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        cnt_map1 = defaultdict(int)
        cnt_map2 = defaultdict(int)
        res = []

        for n in nums1:
            cnt_map1[n] += 1

        for n in nums2:
            cnt_map2[n] += 1

        intersect_key = (set(cnt_map1.keys()) & set(cnt_map2.keys()))

        for n in intersect_key:
            res += [n] * min(cnt_map1[n], cnt_map2[n])
        
        return res
    
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        cnt_map = defaultdict(int)
        res = []

        for n in nums1:
            cnt_map[n] += 1
        
        for n in nums2:
            if cnt_map[n] > 0:
                res.append(n)
                cnt_map[n] -= 1
        
        return res
    
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        cnt_map = defaultdict(int)
        k = 0

        for n in nums1:
            cnt_map[n] += 1
        
        for n in nums2:
            if cnt_map[n] > 0:
                nums1[k] = n
                k += 1
                cnt_map[n] -= 1
        
        return nums1[:k]

        
print(Solution().intersect([1,2,2,1], [2,2]))
print(Solution().intersect([4,9,5], [9,4,9,8,4]))