from collections import defaultdict, deque

class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, k) -> list[int]:

        def add_parent(cur, parent):
            if cur:
                cur.parent = parent
                add_parent(cur.left, cur)
                add_parent(cur.right, cur)
        
        add_parent(root, None)

        ans = []
        visit = set()
        def dfs(cur, dis):
            if cur == None or cur in visit:
                return
            visit.add(cur)
            if dis == 0:
                ans.append(cur.val)
                return
            
            dfs(cur.left, dis - 1)
            dfs(cur.right, dis - 1)
            dfs(cur.parent, dis - 1)
        
        dfs(target, k)
        return ans
    
class Solution:
    graph = defaultdict(list)
    ans = []
    visit = set()

    def buildGraph(self, cur, parent):
        if cur and parent:
            self.graph[cur.val].append(parent.val)
            self.graph[parent.val].append(cur.val)
        if cur.left:
            self.buildGraph(cur.left, cur)
        if cur.right:
            self.buildGraph(cur.right, cur)

    def dfs(self, cur, dis):
        if cur == None or cur in self.visit:
            return
        self.visit.add(cur)
        
        if dis == 0:
            self.ans.append(cur)
            return
        
        for nei in self.graph[cur]:
            if nei not in self.visit:
                self.dfs(nei, dis - 1)



    def distanceK(self, root, target, k) -> list[int]:
        self.graph = defaultdict(list)
        self.buildGraph(root, None)

        self.ans = []
        self.visit = set()

        self.dfs(target.val, k)
        return self.ans
    

class Solution:
    def distanceK(self, root, target, k) -> list[int]:
        graph = defaultdict(list)
        
        def buildGraph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                buildGraph(cur.left, cur)
            if cur.right:
                buildGraph(cur.right, cur)

        buildGraph(root, None)

        ans = []
        visit = set()
        visit.add(target.val)

        def dfs(cur, dis):
            if dis == 0:
                ans.append(cur)
                return
            
            for nei in graph[cur]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei, dis - 1)

        dfs(target.val, k)
        return ans
    
class Solution:
    def distanceK(self, root, target, k) -> list[int]:
        graph = defaultdict(list)

        def buildGraph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            
            if cur.left:
                buildGraph(cur.left, cur)
            if cur.right:
                buildGraph(cur.right, cur)

        buildGraph(root, None)

        ans = []
        visit = set()
        q = deque()
        q.append((target.val, 0))
        visit.add(target.val)

        while q:
            cur, dis = q.popleft()
            if dis == k:
                ans.append(cur)
                continue
            for nei in graph[cur]:
                if nei not in visit:
                    visit.add(nei)
                    q.append((nei, dis+1))
        return ans
        




