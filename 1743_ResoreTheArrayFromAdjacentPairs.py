from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:

        neiborMap = defaultdict(set)
        ans = []
        cur = 0
        now = None
        seen = set()
        N = len(adjacentPairs) + 1

        for x, y in adjacentPairs:
            neiborMap[x].add(y)
            neiborMap[y].add(x)

        for key in neiborMap.keys():
            if len(neiborMap[key]) == 1:
                ans.append(key)
                seen.add(key)
                cur += 1
                now = key
                break

        while cur < N:
            for x in neiborMap[now]:
                if x not in seen:
                    ans.append(x)
                    seen.add(x)
                    cur += 1
                    now = x
                    break
 
        return ans
    

    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        N = len(adjacentPairs) + 1

        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        root = None
        ans = []
        for key in graph.keys():
            if len(graph[key]) == 1:
                root = key
                break
        def dfs(cur, pre):
            ans.append(cur)
            for neibor in graph[cur]:
                if neibor != pre:
                    dfs(neibor, cur)
            
        dfs(root, N+1)
        return ans
    
    def restoreArray(self, adjacentPairs) -> int:
        graph = defaultdict(list)
        root = None
        N = len(adjacentPairs) + 1
        ans = []
        pre = float('inf')

        for x,y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        for key in graph.keys():
            if len(graph[key]) == 1:
                root = key
                break
        
        while len(ans) < N:
            ans.append(root)
            for neighbor in graph[root]:
                if neighbor != pre:
                    pre = root
                    root = neighbor
                    break
        
        return ans

        
        

    
print(Solution().restoreArray([[2,1],[3,4],[3,2]]))
print(Solution().restoreArray([[4,-2],[1,4],[-3,1]]))
print(Solution().restoreArray([[100000,-100000]]))



        
        
        
        