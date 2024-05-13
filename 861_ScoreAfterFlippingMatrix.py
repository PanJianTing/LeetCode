class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        for i in range(M):
            if grid[i][0] == 0:
                for j in range(N):
                    grid[i][j] = 0 if grid[i][j] else 1
        
        for j in range(N):
            zero_cnt = 0
            one_cnt = 0
            for i in range(M):
                if grid[i][j]:
                    one_cnt += 1
                else:
                    zero_cnt += 1
            if zero_cnt > one_cnt:
                for i in range(M):
                    grid[i][j] = 0 if grid[i][j] else 1
        res = 0
        for i in range(M):
            cur = 1
            temp = 0
            for j in range(N-1, -1, -1):
                temp += grid[i][j] * cur
                cur <<= 1
            res += temp
        return res
    

    def matrixScore(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        res = (1 << (N-1)) * M

        cur_power = 1
        for j in range(N-1, 0, -1):
            one_bits = 0
            for i in range(M):
                if grid[i][j] == grid[i][0]:
                    one_bits += 1
            
            max_one_bits = max(one_bits, M-one_bits)
            res += max_one_bits * cur_power
            cur_power <<= 1
        return res

    
print(Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))