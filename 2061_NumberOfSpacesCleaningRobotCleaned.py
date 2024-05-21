from collections import deque

class Solution:
    def numberOfCleanRooms(self, room: list[list[int]]) -> int:
        M = len(room)
        N = len(room[0])
        turn_map = {
            (0, 1)  : (1, 0),
            (1, 0)  : (0, -1),
            (0, -1) : (-1, 0),
            (-1, 0) : (0, 1),
        }

        visited = set()
        res = 0
        q = deque()
        q.append((0, 0))
        cur_dir = (0, 1)
        visited.add(((0,0), cur_dir))
        clean = set()


        while q:
            cur_i, cur_j = q.popleft()
            
            if (cur_i, cur_j) not in clean:
                res += 1
                clean.add((cur_i, cur_j))

            next_i = cur_i + cur_dir[0] 
            next_j = cur_j + cur_dir[1]

            for _ in range(4):
                if not (next_i >= M or next_i < 0 or next_j >= N or next_j < 0 or room[next_i][next_j] == 1):
                    break
                cur_dir = turn_map[cur_dir]
                next_i = cur_i + cur_dir[0] 
                next_j = cur_j + cur_dir[1]

            if 0 <= next_i < M and 0 <= next_j < N  and room[next_i][next_j] == 0 and ((next_i, next_j), cur_dir) not in visited:
                q.append((next_i, next_j))
                visited.add(((next_i, next_j), cur_dir))

        return res
    
        

print(Solution().numberOfCleanRooms([[0,0,0],[1,1,0],[0,0,0]]))
print(Solution().numberOfCleanRooms([[0,0,0],[0,0,0],[0,0,0]]))
print(Solution().numberOfCleanRooms([[0,1,0],[1,0,0],[0,0,0]]))
print(Solution().numberOfCleanRooms([[0,0,0,1],[0,1,0,1],[1,0,0,0]]))