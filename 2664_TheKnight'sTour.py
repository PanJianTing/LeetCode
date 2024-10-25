class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> list[list[int]]:
        dir = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        res = [[0] * n for _ in range(m)]
        res[r][c] = -1

        def dp(cur_r, cur_c, move_cnt):
            if move_cnt == m * n:
                return True
            
            for dr, dc in dir:
                new_r = cur_r + dr
                new_c = cur_c + dc
                if 0 <= new_r < m and 0 <= new_c < n and res[new_r][new_c] == 0:
                    res[new_r][new_c] = move_cnt
                    
                    if dp(new_r, new_c, move_cnt + 1):
                        return True
                    res[new_r][new_c] = 0
            
            return False
        
        dp(r, c, 1)
        res[r][c] = 0
        return res
    
# print(Solution().tourOfKnight(1, 1, 0, 0))
print(Solution().tourOfKnight(3, 4, 0, 0))