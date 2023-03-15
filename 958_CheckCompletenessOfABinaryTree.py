from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:

        
        if root == None:
            return True
        
        q = deque()
        q.append(root)

        foundNull = False

        while len(q) != 0:

            node = q.popleft()

            if node == None:
                foundNull = True
            else:
                if foundNull:
                    return False
                q.append(node.left)
                q.append(node.right)
                

        return True
    
    def isCompleteTree(self, root: TreeNode) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1

        print(bfs)
        return not any(bfs[i:])
    
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = deque()
        q.append(root)
        
        while True:
            node = q.popleft()
            
            if node.left == None:
                if node.right != None:
                    return False
                break

            q.append(node.left)
            if node.right == None:
                break
            q.append(node.right)
        
        while q:
            node = q.popleft()
            if node.left != None or node.right != None:
                return False
        return True 

class Solution:

    def nodeCount(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + self.nodeCount(root.left) + self.nodeCount(root.right)
    
    def dfs(self, root: TreeNode, index: int, n: int) -> bool:
        if root == None:
            return True
        
        if index >= n:
            return False
        return self.dfs(root.left, 2*index + 1, n) and self.dfs(root.right, 2*index + 2, n)
        

    def isCompleteTree(self, root: TreeNode) -> bool:
        return self.dfs(root, 0, self.nodeCount(root))
    

    def isCompleteTree(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root: return 0
            l, r = dfs(root.left), dfs(root.right)
            print(root.val, l, r)
            if l & (l + 1) == 0 and l / 2 <= r <= l:
                return l + r + 1
            if r & (r+1) == 0 and r <= l <= r * 2 + 1:
                return l + r + 1
            
            return -1
        
        return dfs(root) > 0