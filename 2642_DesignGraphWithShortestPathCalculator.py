from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.adj = defaultdict(list)
        self.N = n

        for f, t, cost in edges:
            self.adj[f].append((t, cost))

        # print(self.adj)

    def addEdge(self, edge: list[int]):
        self.adj[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:

        visited = [False] * self.N
        cost = [float('inf')] * self.N
        q = []
        
        cost[node1] = 0 
        heapq.heappush(q, (0, node1))

        while q:
            curCost, curNode = heapq.heappop(q)
            visited[curNode] = True

            for nei, neiCost in self.adj[curNode]:
                if visited[nei] == False:
                    temp = neiCost + curCost
                    heapq.heappush(q, (temp, nei))
                    cost[nei] = min(cost[nei], temp)

        return -1 if cost[node2] == float('inf') else cost[node2]
    
class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.adj = defaultdict(list)
        self.N = n

        for f, t, cost in edges:
            self.adj[f].append((t, cost))

        # print(self.adj)

    def addEdge(self, edge: list[int]):
        self.adj[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:

        cost = [float('inf')] * self.N
        q = []
        
        cost[node1] = 0 
        heapq.heappush(q, (0, node1))

        while q:
            curCost, curNode = heapq.heappop(q)
            if curNode == node2:
                return curCost
            if curCost > cost[curNode]:
                continue

            for nei, neiCost in self.adj[curNode]:
                temp = neiCost + curCost
                if temp < cost[nei]:
                    heapq.heappush(q, (temp, nei))
                    cost[nei] = min(cost[nei], temp)

        return -1


    

g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])

print(g.shortestPath(3,2))
print(g.shortestPath(0,3))
g.addEdge([1,3,4])
print(g.shortestPath(0,3))


g = Graph(13,[[7,2,131570],[9,4,622890],[9,1,812365],[1,3,399349],[10,2,407736],[6,7,880509],[1,4,289656],[8,0,802664],[6,4,826732],[10,3,567982],[5,6,434340],[4,7,833968],[12,1,578047],[8,5,739814],[10,9,648073],[1,6,679167],[3,6,933017],[0,10,399226],[1,11,915959],[0,12,393037],[11,5,811057],[6,2,100832],[5,1,731872],[3,8,741455],[2,9,835397],[7,0,516610],[11,8,680504],[3,11,455056],[1,0,252721]])
print(g.shortestPath(9, 3))