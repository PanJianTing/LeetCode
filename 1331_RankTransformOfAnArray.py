class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:

        sortArr = sorted(set(arr))
        rankMap = {}

        rank = []

        for i, count in enumerate(sortArr):

            rankMap[count] = i + 1

        for count in arr:
            rank.append(rankMap[count])


        return rank