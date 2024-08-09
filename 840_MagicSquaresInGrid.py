class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        res = 0

        for r in range(0, R-2):
            for c in range(0, C-2):
                temp = set()
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if 1 <= grid[i][j] <= 9:
                            temp.add(grid[i][j])
                
                if len(temp) == 9 and grid[r+1][c+1] == 5:
                    diagonal1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
                    diagonal2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]

                    row1 = grid[r][c] + grid[r][c+1] + grid[r][c+2]
                    row2 = grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2]
                    row3 = grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]

                    col1 = grid[r][c] + grid[r+1][c] + grid[r+2][c]
                    col2 = grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]
                    col3 = grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]

                    if diagonal1 == diagonal2 == row1 == row2 == row3 == col1 == col2 == col3:
                        res += 1

        return res
    
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        res = 0

        for r in range(0, R-2):
            for c in range(0, C-2):
                temp = [0] * 9
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if 1 <= grid[i][j] <= 9:
                            temp[3 * (i-r) + (j-c)] = str(grid[i][j])
                
                check_str = "".join([temp[0], temp[1], temp[2], temp[5], temp[8], temp[7], temp[6], temp[3]])

                if 0 == (int(temp[0][0]) & 1) and (check_str in "2943816729438167" or check_str in "7618349276183492") and temp[4] == "5":
                    res += 1
                
        return res
    
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        res = 0

        for r in range(0, R-2):
            for c in range(0, C-2):
                border_idx = [0,1,2,5,8,7,6,3]
                border_list = []

                for idx in border_idx:
                    num = grid[r + (idx // 3)][c + (idx % 3)]
                    border_list.append(str(num))
                        
                check_str = "".join(border_list)

                if 0 == (int(grid[r][c]) & 1) and (check_str in "2943816729438167" or check_str in "7618349276183492") and grid[r+1][c+1] == 5:
                    res += 1
        return res

print(Solution().numMagicSquaresInside([[4,7,8],[9,5,1],[2,3,6]]))
print(Solution().numMagicSquaresInside([[8,1,6],[3,5,7],[4,9,2]]))
print(Solution().numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
print(Solution().numMagicSquaresInside([[8]]))