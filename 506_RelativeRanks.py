class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[int]:
        sortScore = sorted(score, reverse=True)

        ranks = {}

        for rank, sc in enumerate(sortScore):
            if rank == 0:
                ranks[sc] = "Gold Medal"
            elif rank == 1:
                ranks[sc] = "Silver Medal"
            elif rank == 2:
                ranks[sc] = "Bronze Medal"
            else:
                ranks[sc] = str(rank + 1)
        return [ranks[i] for i in score]


    def findRelativeRanks_my(self, score: list[int]) -> list[int]:
        sortScore = sorted(score, reverse=True)

        for i in range(len(score)):
            sc = score[i]
            rank = sortScore.index(sc)
            if rank == 0:
                score[i] = "Gold Medal"
            elif rank == 1:
                score[i] = "Silver Medal"
            elif rank == 2:
                 score[i] = "Bronze Medal"
            else:
                score[i] = str(rank+1)
        return score


Solution.findRelativeRanks(Solution(), [5,4,3,2,1])