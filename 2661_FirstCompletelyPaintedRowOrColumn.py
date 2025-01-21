from collections import defaultdict

class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        N = len(arr)
        ROW = len(mat)
        COL = len(mat[0])

        num_row_map = defaultdict(int)
        num_col_map = defaultdict(int)

        row_cnt_list = [0] * ROW
        col_cnt_list = [0] * COL

        for r in range(ROW):
            for c in range(COL):
                cur_n = mat[r][c]
                num_row_map[cur_n] = r
                num_col_map[cur_n] = c

        for i, n in enumerate(arr):
            row_idx = num_row_map[n]
            col_idx = num_col_map[n]

            row_cnt_list[row_idx] += 1
            col_cnt_list[col_idx] += 1

            if row_cnt_list[row_idx] == COL:
                return i

            if col_cnt_list[col_idx] == ROW:
                return i
        
        return -1
    
print(Solution().firstCompleteIndex([1,4,5,2,6,3], [[4,3,5],[1,2,6]]))