from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

#my
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        q = deque()
        if root == None:
            return True
        
        q.append(root)

        while len(q) > 0:
            k = len(q)
            nodes = []
            for _ in range(0,k):

                node = q.popleft()
                if node == None:
                    nodes.append(TreeNode(-1000))
                else:
                    nodes.append(node)
                    q.append(node.left)
                    q.append(node.right)
                    
            l = 0
            r = k - 1
            
            while l <= r:
                nodeL = nodes[l]
                nodeR = nodes[r]

                if nodeL.val != nodeR.val:
                    return False
                
                l += 1
                r -= 1
        return True


# recursion   
class Solution:
    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None and t2 == None: return True
        if t1 == None or t2 == None: return False
        return (t1.val == t2.val) and (self.isMirror(t1.left, t2.right)) and (self.isMirror(t1.right, t2.left))

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

# iterative
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        q = deque()
        q.append(root)
        q.append(root)

        while len(q) > 0:
            t1 = q.popleft()
            t2 = q.popleft()

            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)

        return True


            



