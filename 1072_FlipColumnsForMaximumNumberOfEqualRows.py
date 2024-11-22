from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        ans = 0
        
        for cur_row in matrix:
            temp = 0
            flip_row = []

            for i in range(COL):
                if cur_row[i] == 1:
                    flip_row.append(0)
                else:
                    flip_row.append(1)

            for compare_row in matrix:
                if cur_row == compare_row or flip_row == compare_row:

                    temp += 1
            ans = max(ans, temp)

        return ans
    
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])

        patter_map = defaultdict(int)

        for cur_row in matrix:
            symbol = cur_row[0]
            symbol_str = []

            for c in range(COL):
                if symbol == cur_row[c]:
                    symbol_str.append("T")
                else:
                    symbol_str.append("F")
            
            cur_str = ''.join(symbol_str)
            patter_map[cur_str] += 1
        
        return max(patter_map.values())


# print(Solution().maxEqualRowsAfterFlips([[0,1],[1,1]]))
print(Solution().maxEqualRowsAfterFlips([[0,1],[1,0]]))