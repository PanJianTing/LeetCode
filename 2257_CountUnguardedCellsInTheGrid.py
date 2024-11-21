class Solution:

    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        ans = m * n
        visit = set()
        temp_walls = set()
        temp_g = set()
        
        for i, j in walls:
            temp_walls.add((i, j))

        for i, j in guards:
            temp_g.add((i, j))

        walls = temp_walls

        for i, j in guards:

            for k in range(i+1, m):
                if (k, j) in temp_g:
                    break

                if (k, j) in walls:
                    break
                else:
                    visit.add((k, j))
            
            for k in range(i-1, -1, -1):
                if (k, j) in temp_g:
                    break

                if (k, j) in walls:
                    break
                else:
                    visit.add((k, j))
            
            for k in range(j-1, -1, -1):
                if (i, k) in temp_g:
                    break

                if (i, k) in walls:
                    break
                else:
                    visit.add((i, k))

            for k in range(j+1, n):
                if (i, k) in temp_g:
                    break

                if (i, k) in walls:
                    break
                else:
                    visit.add((i, k))

        return ans - len(temp_g | walls | visit)
    
    def countUnguarded(self, rows: int, cols: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        WALL = 1
        GUARD = 2
        GUARDED = 3
        UNGUARDED = 4
        ans = 0
        grids = [[UNGUARDED] * cols for _ in range(rows)]

        
        for i, j in walls:
            grids[i][j] = WALL

        for i, j in guards:
            grids[i][j] = GUARD

        for g_r, g_c in guards:

            for r in range(g_r+1, rows):
                if grids[r][g_c] == WALL or grids[r][g_c] == GUARD:
                    break
                grids[r][g_c] = GUARDED
            
            for r in range(g_r-1, -1, -1):
                if grids[r][g_c] == WALL or grids[r][g_c] == GUARD:
                    break
                grids[r][g_c] = GUARDED

            for c in range(g_c+1, cols):
                if grids[g_r][c] == WALL or grids[g_r][c] == GUARD:
                    break
                grids[g_r][c] = GUARDED
            
            for c in range(g_c-1, -1, -1):
                if grids[g_r][c] == WALL or grids[g_r][c] == GUARD:
                    break
                grids[g_r][c] = GUARDED
        
        for r in range(rows):
            for c in range(cols):
                if grids[r][c] == UNGUARDED:
                    ans += 1

        return ans
            


# print(Solution().countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]))
# print(Solution().countUnguarded(2, 7, [[1,5],[1,1],[1,6],[0,2]], [[0,6],[0,3],[0,5]]))
print(Solution().countUnguarded(8, 9, [[5,8],[5,5],[4,6],[0,5],[6,5]], [[4,1]]))