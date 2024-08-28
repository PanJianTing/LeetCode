from collections import defaultdict, deque

class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        M = len(grid1)
        N = len(grid1[0])
        ans = 0

        def find_lands(grid):
            q = deque()
            all_lands = []

            for i in range(M):
                for j in range(N):
                    if grid[i][j]:
                        lands = set()
                        q.append((i, j))
                        lands.add((i, j))
                        grid[i][j] = 0

                        while q:
                            cur_i, cur_j = q.popleft()

                            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                next_i = cur_i + di
                                next_j = cur_j + dj
                                if 0 <= next_i < M and 0 <= next_j < N and grid[next_i][next_j]:
                                    lands.add((next_i, next_j))
                                    grid[next_i][next_j] = 0
                                    q.append((next_i, next_j))

                        all_lands.append(lands)
            return all_lands
        
        # all_land1 = find_lands(grid1)
        all_land2 = find_lands(grid2)

        for land in all_land2:
            is_sub = True
            for i, j in land:
                if grid1[i][j] == 0:
                    is_sub = False
                    break
            if is_sub:
                ans += 1
        return ans
    
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        M = len(grid2)
        N = len(grid2[0])
        ans = 0

        for i in range(M):
            for j in range(N):
                if grid2[i][j]:
                    q = deque()
                    is_sub_island = (grid1[i][j] == 1)
                    q.append((i, j))

                    while q:
                        cur_i, cur_j = q.popleft()

                        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            next_i = cur_i + di
                            next_j = cur_j + dj
                            if 0 <= next_i < M and 0 <= next_j < N and grid2[next_i][next_j]:
                                if grid1[next_i][next_j] == 0:
                                    is_sub_island = False
                                
                                grid2[next_i][next_j] = 0
                                q.append((next_i, next_j))

                    if is_sub_island:
                        ans += 1

        return ans
    

    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        M = len(grid2)
        N = len(grid2[0])
        ans = 0

        def dfs(cur_i, cur_j):

            is_sub = grid2[cur_i][cur_j] & grid1[cur_i][cur_j]
            grid2[cur_i][cur_j] = 0

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_i = cur_i + di
                next_j = cur_j + dj
                if 0 <= next_i < M and 0 <= next_j < N and grid2[next_i][next_j]:
                    is_sub = is_sub & dfs(next_i, next_j)
            
            return is_sub

        for i in range(M):
            for j in range(N):
                if grid2[i][j]:
                    if dfs(i, j):
                        ans += 1

        return ans



    
print(Solution().countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))
print(Solution().countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))
                        



