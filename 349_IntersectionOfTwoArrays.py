
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        set1 = set(nums1)
        set2 = set(nums2)

        return set1 & set2


    def intersection_my(self, nums1: list[int], nums2: list[int]) -> list[int]:
        resultList = set()

        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    resultList.add(num1)

        return resultList

print(Solution.intersection(Solution(), [1,2,2,1], [2,2]))