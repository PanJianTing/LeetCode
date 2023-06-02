from collections import deque

class Solution:

    def maximumDetonation(self, b: list[list[int]]) -> int:

        def bfs(idx, now):

            q = deque()
            visit = set()
            x, y, r = now
            visit.add(idx)
            q.append(now)
            res = 1

            while q:
                x,y,r = q.popleft()

                # y0 = y-r
                # y1 = y+r
                # x0 = x-r
                # x1 = x+r
                dis = r ** 2

                for i, (nei_x, nei_y, nei_r) in enumerate(b):
                    if i in visit:
                        continue
                    else:
                        if dis >= ((nei_x - x) ** 2 + (nei_y - y) ** 2):
                            q.append((nei_x, nei_y, nei_r))
                            visit.add(i)
                            res += 1

            return res
        
        return max([bfs(i, t) for i, t in enumerate(b)])


                


                        