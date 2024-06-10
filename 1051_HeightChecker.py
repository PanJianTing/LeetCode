class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        N = len(heights)
        expected = sorted(heights)
        res = 0

        for i in range(N):
            if expected[i] != heights[i]:
                res += 1
        return res
    

print(Solution().heightChecker([1,1,4,2,1,3]))