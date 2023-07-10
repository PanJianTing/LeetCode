from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val= 0, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        q = deque()
        q.append(root)
        dep = 1

        while q:
            
            cnt = len(q)
            for _ in range(cnt):
                cur = q.popleft()
                if cur.left == None and cur.right == None:
                    return dep
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            dep += 1
        
        return dep
    
    def dfs(self, root) -> int:
        if root == None:
            return 0
        
        if root.right and root.left:
            return 1 + min(self.dfs(root.right), self.dfs(root.left))
        
        if root.right:
            return 1 + self.dfs(root.right)
        
        if root.left:
            return 1 + self.dfs(root.left)
        
        return 1

    def dfs(self, root) -> int:
        if root == None:
            return 0
        
        if root.left == None:
            return 1 + self.dfs(root.right)
        elif root.right == None:
            return 1 + self.dfs(root.left)
        
        return 1 + min(self.dfs(root.right), self.dfs(root.left))


    def minDepth(self, root: TreeNode) -> int:
        return self.dfs(root)
    
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        q = deque()
        q.append(root)
        dep = 1

        while q:
            
            cnt = len(q)
            for _ in range(cnt):
                cur = q.popleft()
                if cur == None:
                    continue

                if cur.left == None and cur.right == None:
                    return dep
                
                q.append(cur.left)
                q.append(cur.right)
            dep += 1
        
        return dep
    

    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        leftD = self.minDepth(root.left)
        rightD = self.minDepth(root.right)
        return leftD + rightD + 1 if (leftD == 0 or rightD == 0) else min(leftD, rightD) + 1
    

    def minDepth(self, root: TreeNode) -> int:
        q = [(root, 1)]
        while q:
            curr, depth = q.pop(0)
            if curr is None:
                continue
            if curr.left == None and curr.right == None:
                return depth
            q.append((curr.left, depth + 1))
            q.append((curr.right, depth + 1))
        return 0

    

            



        