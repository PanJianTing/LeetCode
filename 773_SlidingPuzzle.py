from collections import deque, defaultdict
from functools import cache

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        ROW = 2
        COL = 3

        q = deque()
        q.append
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        puzzle = '123450'
        visit = set()

        def list_to_str(cur_board):
            cur_str = []
            for r in range(ROW):
                for c in range(COL):
                    cur_str.append(str(cur_board[r][c]))
            
            return "".join(cur_str)
        
        def str_to_list(cur_str):
            return_board = [[0] * 3 for i in range(2)]

            for i, c in enumerate(cur_str):
                return_board[i//3][i%3] = int(c)
            
            return return_board


        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 0:
                    q.append((r, c, list_to_str(board), 0))
        
        while q:
            cur_r, cur_c, now_str, cur_cnt = q.popleft()

            if now_str == puzzle:
                return cur_cnt

            visit.add(now_str)

            for dr, dc in dirs:
                cur_b = str_to_list(now_str)
                next_r = cur_r + dr
                next_c = cur_c + dc

                if 0 <= next_r < ROW and 0 <= next_c < COL:
                    cur_b[cur_r][cur_c], cur_b[next_r][next_c] = cur_b[next_r][next_c], cur_b[cur_r][cur_c]
                    next_str = list_to_str(cur_b)
                    if next_str not in visit:
                        q.append((next_r, next_c, next_str, cur_cnt+1))
        
        return -1
    

    def slidingPuzzle(self, board: list[list[int]]) -> int:

        dirs = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        def swap(s, i, j):
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            return "".join(s_list)
        
        start_state = ''.join([str(n) for row in board for n in row])

        visited = defaultdict(int)

        @cache
        def dfs(state, zero_pos, moves):
            if state in visited and visited[state] <= moves:
                return
            
            visited[state] = moves

            for next_pos in dirs[zero_pos]:
                new_state = swap(state, zero_pos, next_pos)
                dfs(new_state, next_pos, moves+1)
            
            return
        dfs(start_state, start_state.index('0'), 0)

        return visited['123450']  if '123450' in visited else -1
    
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        ROW = 2
        COL = 3

        dirs = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        def swap(s, i, j):
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            return ''.join(s_list)
        
        start_state = ''.join([str(board[r][c]) for r in range(ROW) for c in range(COL)])
        target = '123450'
        q = deque()
        q.append(start_state)

        move = 0
        visit = set()

        while q:
            cur_cnt = len(q)

            for _ in range(cur_cnt):
                cur_state = q.popleft()
                zero_pos = cur_state.index('0')

                if cur_state == target:
                    return move
                
                visit.add(cur_state)

                for next_pos in dirs[zero_pos]:
                    next_state = swap(cur_state, zero_pos, next_pos)

                    if next_state not in visit:
                        q.append(next_state)
            
            move += 1
        return -1
    

print(Solution().slidingPuzzle([[1,2,3],[4,0,5]]))
print(Solution().slidingPuzzle([[1,2,3],[5,4,0]]))
print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))




