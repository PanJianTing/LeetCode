class Solution:
    def numEquivDominoPairs(self, dominos: list[list[int]]) -> int:
        pairs = 0
        dominoDic = {}

        for domino in dominos:
            if domino[0] > domino[1]:
                domino[0], domino[1] = domino[1], domino[0]

            tupleDomino = tuple(domino)

            if tuple(domino) in dominoDic:
                dominoDic[tupleDomino] += 1
            else:
                dominoDic[tupleDomino] = 1

        for k, obj in dominoDic.items():
            pairs += obj * (obj - 1) //2

        return pairs




    def numEquivDominoPairs_timeout(self, dominoes: list[list[int]]) -> int:

        pair = 0

        for i in range(len(dominoes)):
            for j in range(i+1, len(dominoes)):
                dominoeI = dominoes[i]
                dominoeJ = dominoes[j]

                if dominoeI[0] == dominoeJ[0] and dominoeI[1] == dominoeJ[1]:
                    pair += 1
                elif dominoeI[0] == dominoeJ[1] and dominoeI[1] == dominoeJ[0]:
                    pair += 1

        return pair

Solution.numEquivDominoPairs(Solution(), [[1,2],[2,1],[3,4],[5,6]])