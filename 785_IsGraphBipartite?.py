class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}
        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
    
    def check(self, graph: list[list[int]], start: int, seen: dict) -> bool:
        q = [(start, 1)]
        while len(q):
            pop, color = q.pop(0)
            if pop in seen:
                if seen[pop] != color:
                    return False
                continue

    def isBipartite(self, graph: list[list[int]]) -> bool:
        seen = {}

        for i in range(len(graph)):
            if i not in seen:
        