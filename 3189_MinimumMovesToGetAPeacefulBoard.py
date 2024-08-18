class Solution:
    def minMoves(self, rooks: list[list[int]]) -> int:
        N = len(rooks)
        res = 0

        rooks.sort(key= lambda x: x[0])

        for i in range(N):
            res += abs(i - rooks[i][0])
        
        rooks.sort(key= lambda x: x[1])

        for i in range(N):
            res += abs(i - rooks[i][1])
        
        return res
    
    def minMoves(self, rooks: list[list[int]]) -> int:
        N = len(rooks)
        res = 0
        row_cnts = [0] * N
        col_cnts = [0] * N

        for r, c in rooks:
            row_cnts[r] += 1
            col_cnts[c] += 1

        row_moves = 0
        col_moves = 0
        for i in range(N):
            row_moves += row_cnts[i] - 1
            col_moves += col_cnts[i] - 1

            res += abs(row_moves) + abs(col_moves)
        return res
    
print(Solution().minMoves([[0,0],[1,0],[1,1]]))
print(Solution().minMoves([[0,0],[0,1],[0,2],[0,3]]))
