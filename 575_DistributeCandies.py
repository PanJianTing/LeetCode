class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:

        allType = len(set(candyType))

        maxCountCandy = len(candyType) // 2

        if allType > maxCountCandy:
            return maxCountCandy
        return allType


Solution.distributeCandies(Solution(), [6,6,6,6])