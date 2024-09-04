class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        temp = set()
        for x, y in obstacles:
            temp.add((x, y))
        obstacles = temp
        dir = (0, 1)
        cur = (0, 0)
        res = 0 

        for c in commands:
            if c == -1:
                if dir == (0, 1):
                    dir = (1, 0)
                elif dir == (1, 0):
                    dir = (0, -1)
                elif dir == (0, -1):
                    dir = (-1, 0)
                else:
                    dir = (0, 1)
            elif c == -2:
                if dir == (0, 1):
                    dir = (-1, 0)
                elif dir == (-1, 0):
                    dir = (0, -1)
                elif dir == (0, -1):
                    dir = (1, 0)
                else:
                    dir = (0, 1)
            else:
                dx, dy = dir
                cur_x, cur_y = cur

                for _ in range(c):
                    cur_x += dx
                    cur_y += dy
                    if (cur_x, cur_y) in obstacles:
                        cur_x -= dx
                        cur_y -= dy
                        break
                
                res = max(res, (cur_x ** 2 + cur_y ** 2))
                cur = (cur_x, cur_y)

        return res
    

    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        temp = set()
        for x, y in obstacles:
            temp.add((x, y))
        obstacles = temp
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir = 0
        cur_dx = 0
        cur_dy = 1
        cur_x = 0
        cur_y = 0
        res = 0 

        for c in commands:
            if c == -1:
                cur_dir += 1
                cur_dir %= 4
                cur_dx, cur_dy = dirs[cur_dir]
            elif c == -2:
                cur_dir += 3
                cur_dir %= 4
                cur_dx, cur_dy = dirs[cur_dir]
            else:
                
                for _ in range(c):
                    cur_x += cur_dx
                    cur_y += cur_dy
                    if (cur_x, cur_y) in obstacles:
                        cur_x -= cur_dx
                        cur_y -= cur_dy
                        break
                res = max(res, (cur_x ** 2 + cur_y ** 2))

        return res
    
print(Solution().robotSim([4,-1,3], []))
print(Solution().robotSim([4,-1,4,-2,4], [[2,4]]))
print(Solution().robotSim([6,-1,-1,6], []))

