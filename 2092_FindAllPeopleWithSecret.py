from collections import deque
from collections import defaultdict
import heapq

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        q = deque()
        adj_map = defaultdict(list)
        know_time = [float('inf')] * n
        ans = []


        for p1, p2, t in meetings:
            adj_map[p1].append((t, p2))
            adj_map[p2].append((t, p1))
        
        q.append((0, 0))
        q.append((0, firstPerson))
        know_time[0] = 0
        know_time[firstPerson] = 0

        while q:
            cur_t, cur_p = q.popleft()
            
            for next_t, next_p in adj_map[cur_p]:
                if next_t >= cur_t and next_t < know_time[next_p]:
                    know_time[next_p] = next_t
                    q.append((next_t, next_p))


        return [i for i in range(n) if know_time[i] != float('inf')]

print(Solution().findAllPeople(12, [[10,8,6],[9,5,11],[0,5,18],[4,5,13],[11,6,17],[0,11,10],[10,11,7],[5,8,3],[7,6,16],[3,6,10],[3,11,1],[8,3,2],[5,0,7],[3,8,20],[11,0,20],[8,3,4],[1,9,4],[10,7,11],[8,10,18]], 9))