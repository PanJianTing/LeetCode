from collections import defaultdict

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        set1 = set(nums1)
        set2 = set(nums2)

        return set1 & set2


    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        resultList = set()

        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    resultList.add(num1)

        return resultList
    
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        N1 = len(nums1)
        N2 = len(nums2)
        p1 = 0
        p2 = 0
        nums1.sort()
        nums2.sort()
        ans = set()

        while p1 < N1 and p2 < N2:
            if nums1[p1] == nums2[p2]:
                ans.add(nums1[p1])
                p1 += 1
                p2 += 1
            else:
                if nums1[p1] < nums2[p2]:
                    p1 += 1
                else:
                    p2 += 1
        return ans
    

    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        cnt_map1 = defaultdict(int)
        res = set()

        for n in nums1:
            cnt_map1[n] += 1
        
        for n in nums2:
            if cnt_map1[n] > 0:
                res.add(n)
        return res



print(Solution.intersection(Solution(), [1,2,2,1], [2,2]))