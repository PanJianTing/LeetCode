class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        res = 0

        move_dot = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                    (-1, -1), (-1, 1), (1, -1), (1, 1), 
                    (-1, -2), (1, -2), (-1, 2), (1, 2),
                    (-2, -1), (-2, 1), (2, -1), (2, 1)]
        
        skip_dot = [(0, -2), (2, 0), (0, 2), (-2, 0), 
                    (-2, -2), (2, -2), (2, 2), (-2, 2)]
        
        def backtract(cur_x, cur_y, cur_length, visit):
            if cur_length > n:
                return 0
            
            valid_count = 0
            visit[cur_y][cur_x] = True
            
            if cur_length >= m:
                valid_count += 1

            for dx, dy in move_dot:
                next_x = cur_x + dx
                next_y = cur_y + dy

                if 0 <= next_x < 3 and 0 <= next_y < 3 and visit[next_y][next_x] == False:
                    valid_count += backtract(next_x, next_y, cur_length + 1, visit)
            
            for dx, dy in skip_dot:
                next_x = cur_x + dx
                next_y = cur_y + dy
                middle_x = cur_x + (dx >> 1)
                middle_y = cur_y + (dy >> 1)
                if 0 <= next_x < 3 and 0 <= next_y < 3 and visit[next_y][next_x] == False:
                    if visit[middle_y][middle_x]:
                        valid_count += backtract(next_x, next_y, cur_length + 1, visit)

            visit[cur_y][cur_x] = False

            return valid_count
        
        for i in range(3):
            for j in range(3):
                visit = [[False] * 3 for _ in range(3)]
                res += backtract(i, j, 1, visit)
        return res
    
    def numberOfPatterns(self, m: int, n: int) -> int:
        print(1 << 10)
        res = 0
        jump_matrix = [[0] * 10 for _ in range(10)]

        jump_matrix[1][3] = jump_matrix[3][1] = 2
        jump_matrix[1][7] = jump_matrix[7][1] = 4
        jump_matrix[1][9] = jump_matrix[9][1] = 5
        jump_matrix[2][8] = jump_matrix[8][2] = 5
        jump_matrix[3][7] = jump_matrix[7][3] = 5
        jump_matrix[3][9] = jump_matrix[9][3] = 6
        jump_matrix[4][6] = jump_matrix[6][4] = 5
        jump_matrix[7][9] = jump_matrix[9][7] = 8

        def backtract(cur, cur_length, visit):

            if cur_length > n:
                return 0
            
            valid = 0
            if cur_length >= m:
                valid += 1

            visit[cur] = True
            
            for next_dot in range(1, 10):
                if visit[next_dot] == False and (jump_matrix[cur][next_dot] == 0 or visit[jump_matrix[cur][next_dot]]):
                    valid += backtract(next_dot, cur_length + 1, visit)
            
            visit[cur] = False
            return valid
        
        res += (backtract(1, 1, [False] * 10) << 2)
        res += (backtract(2, 1, [False] * 10) << 2)
        res += backtract(5, 1, [False] * 10)

        return res
    
print(Solution().numberOfPatterns(1,1))
print(Solution().numberOfPatterns(2,2))
print(Solution().numberOfPatterns(1,2))
print(Solution().numberOfPatterns(3,3))
print(Solution().numberOfPatterns(1,3))