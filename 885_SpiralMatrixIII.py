class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        total = rows * cols
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur = [rStart, cStart]
        cur_dir = 0
        move = 1
        ans = []
        ans.append(cur)
 
        while len(ans) < total:

            for _ in range(move):
                cur_r, cur_c = cur
                next_r = cur_r + dirs[cur_dir][0]
                next_c = cur_c + dirs[cur_dir][1]

                if 0 <= next_r < rows and 0 <= next_c < cols:
                    ans.append([next_r, next_c])
                
                cur = [next_r, next_c]
            if cur_dir == 1 or cur_dir == 3:
                move += 1

            cur_dir = (cur_dir + 1) % 4
            # cur_dir += 1
            # if cur_dir == 4:
            #     cur_dir = 0

        return ans
    

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        step = 1
        cur_dir = 0
        curR = rStart
        curC = cStart
        ans = [[curR, curC]]

        while len(ans) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    curR += dirs[cur_dir][0]
                    curC += dirs[cur_dir][1]

                    if 0 <= curR < rows and 0 <= curC < cols:
                        ans.append([curR, curC])
                
                cur_dir = (cur_dir + 1) % 4
            
            step += 1

        return ans
    
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        step = 1
        curR = rStart
        curC = cStart
        ans = [[curR, curC]]

        while len(ans) < rows * cols:

            for dr, dc, d in [[0, 1, step], [1, 0, step], [0, -1, step + 1], [-1, 0, step + 1]]:
                for _ in range(d):
                    curR += dr
                    curC += dc

                    if 0 <= curR < rows and 0 <= curC < cols:
                        ans.append([curR, curC])
            
            step += 2

        return ans
    
print(Solution().spiralMatrixIII(1, 4, 0, 0))
print(Solution().spiralMatrixIII(5, 6, 1, 4))