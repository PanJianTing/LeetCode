class UnionFind:
    def __init__(self, N) -> None:
        self.parent = list(range(N))
        self.size = [1] * N
        self.max_size = 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.max_size = max(self.max_size, self.size[root_x])
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, N, edges):

        # data structure [[Start_Node, End_Node, Weight, Idx], [Start_Node, End_Node, Weight, Idx], ....]
        new_edges = [edge.copy() for edge in edges]

        for i, edge in enumerate(new_edges):
            edge.append(i)

        # Sort by weight
        new_edges.sort(key=lambda x : x[2])

        # Find Standard MST Weight using Union-Find
        std_uf = UnionFind(N)
        std_weight = 0
        for u, v, w, idx in new_edges:
            if std_uf.union(u, v):
                std_weight += w
            
        critical = []
        pseudo_critical = []
        for u, v, w, i in new_edges:
            ignore_uf = UnionFind(N)
            ignore_weight = 0
            for x, y, w_ignore, j in new_edges:
                if i != j and ignore_uf.union(x, y):
                    ignore_weight += w_ignore
            
            if ignore_uf.max_size < N or ignore_weight > std_weight:
                critical.append(i)
                continue

            force_uf = UnionFind(N)
            force_weight = w
            force_uf.union(u, v)
            for x, y, w_force, j in new_edges:
                if  i != j and force_uf.union(x, y):
                    force_weight += w_force
                
            if force_weight == std_weight:
                pseudo_critical.append(i)
        
        # print(new_edges)

        return [critical, pseudo_critical]
    
print(Solution().findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))
print(Solution().findCriticalAndPseudoCriticalEdges(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]))

