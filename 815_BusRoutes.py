from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target) -> int:
        if source == target:
            return 0

        N = len(routes)
        bus_route = defaultdict(set)
        adj = defaultdict(list)

        for i, r in enumerate(routes):
            bus_route[i] = set(r)

        for i in range(N):
            for j in range(i+1, N):
                if len(bus_route[i].intersection(bus_route[j])):
                    adj[i].append(j)
                    adj[j].append(i)

        q = deque()
        visit = set()
        ans = 9999999
        
        for idx in bus_route.keys():
            if source in bus_route[idx]:
                q.append((idx, 1))
                visit.add(idx)

        while q:
            
            cur_bus, cur_cnt = q.popleft()

            if target in bus_route[cur_bus]:
                ans = min(ans, cur_cnt)
            
            for next in adj[cur_bus]:
                if next not in visit:
                    q.append((next, cur_cnt + 1))
                    visit.add(next)

        return -1 if ans == 9999999 else ans
    

    def numBusesToDestination(self, routes, source, target) -> int:
        if source == target:
            return 0

        N = len(routes)
        bus_route = defaultdict(set)
        adj = defaultdict(list)

        for i, r in enumerate(routes):
            bus_route[i] = set(r)

        for i in range(N):
            for j in range(i+1, N):
                if len(bus_route[i].intersection(bus_route[j])):
                    adj[i].append(j)
                    adj[j].append(i)

        q = deque()
        visit = set()
        
        for idx in bus_route.keys():
            if source in bus_route[idx]:
                q.append((idx, 1))
                visit.add(idx)

        while q:
            
            cur_bus, cur_cnt = q.popleft()

            if target in bus_route[cur_bus]:
                return cur_cnt
            
            for next in adj[cur_bus]:
                if next not in visit:
                    q.append((next, cur_cnt + 1))
                    visit.add(next)

        return -1
    
    def numBusesToDestination(self, routes, source, target) -> int:
        bus_map = defaultdict(list)

        for i, r in enumerate(routes):
            for stop in r:
                bus_map[stop].append(i)
        
        visit = set()
        q = deque()
        
        q.append((source, 0))
        visit.add(source)

        while q:
            cur_stop, cur_cnt = q.popleft()

            if cur_stop == target:
                return cur_cnt

            for next in bus_map[cur_stop]:
                for next_stop in routes[next]:
                    if next_stop not in visit:
                        q.append((next_stop, cur_cnt + 1))
                        visit.add(next_stop)

                routes[next] = []
        return -1
            

print(Solution().numBusesToDestination([[1,2,7], [3,6,7]], 1, 6))
print(Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))

        
        



        
        