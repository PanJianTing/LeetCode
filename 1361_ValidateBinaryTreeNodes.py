from collections import defaultdict, deque


class UnionFind:

    def __init__(self, n):
        self.component = n
        self.parents = list(range(n))

    def union(self, parent, child):
        parent_parent = self.find(parent)
        child_parent = self.find(child)

        # has seen
        if child_parent != child:
            print("false 1")
            return False
        
        # cycle
        if parent_parent == child_parent:
            print("false 2")
            return False
        
        self.component -= 1
        self.parents[child_parent] = parent_parent
        return True 
        

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        
        return self.parents[node]


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        q = deque()
        visit = set()
        st = -1
        childSet = set(rightChild) | set(leftChild)

        for i in range(n):
            if i not in childSet:
                st = i

        if st == -1:
            return False

        q.append(st)
        visit.add(st)

        while q:
            cur = q.popleft()
            
            for nextCurr in [leftChild[cur], rightChild[cur]]:
                if nextCurr != -1:
                    if nextCurr in visit:
                        return False
                    visit.add(nextCurr)
                    q.append(nextCurr)
        
        return len(visit) == n
    
    def validateBinaryTreeNodes(self, n, leftChild, rightChild) -> int:
        
        def findRoot():

            childSet = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in childSet:
                    return i
            return -1
        root = findRoot()
        
        if root == -1:
            return False
        
        st = []
        seen = set()
        st.append(root)
        seen.add(root)

        while st:
            cur = st.pop()

            for child in [leftChild[cur], rightChild[cur]]:
                if child == -1:
                    continue
                
                if child in seen:
                    return False
                
                st.append(child)
                seen.add(child)
        
        return len(seen) == n
    
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):

        uf = UnionFind(n)
        for i in range(n):
            for node in [leftChild[i], rightChild[i]]:
                if node == -1:
                    continue
                if not uf.union(i, node):
                    return False
        
        return uf.component == 1
    



# print(Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1]))
# print(Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1]))
# print(Solution().validateBinaryTreeNodes(2, [1,0], [-1,-1]))
print(Solution().validateBinaryTreeNodes(6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1]))
# print(Solution().validateBinaryTreeNodes(4, [3,-1,1,-1], [-1,-1,0,-1]))
