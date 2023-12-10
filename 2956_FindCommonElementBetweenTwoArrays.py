class Solution:
    def findIntersectionValues(self, n1, n2) -> list[int]:
        n1_set = set(n1)
        n2_set = set(n2)
        ans1 = 0
        ans2 = 0
        for i, n in enumerate(n1):
            if n in n2_set:
                ans1 += 1

        for i, n in enumerate(n2):
            if n in n1_set:
                ans2 += 1
        
        return [ans1, ans2]


print(Solution().findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6]))
print(Solution().findIntersectionValues([3,4,2,3], [1,5]))