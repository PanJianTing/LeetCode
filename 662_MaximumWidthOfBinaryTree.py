from collections import deque

class TreeNode:
    def __init__(self, val= 0, left= None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        ans = 0

        q = deque()
        if root:
            q.append((root, 0))

        while len(q):
            
            cnt = len(q)
            start = end = 0
            for i in range(cnt):
                node, num = q.popleft()
                if i == 0:
                    start = num
                if i == cnt -1:
                    end = num

                if node.left:
                    q.append((node.left, (num << 1) + 1))
                
                if node.right:
                    q.append((node.right, (num << 1) + 2))
            
            ans = max(ans, end - start)
        return ans + 1

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        q = deque()
        if root:
            q.append((root, 1))

        while len(q):
            head, first = q[0]
            cnt = len(q)
            
            end = 0
            for _ in range(cnt):
                node, end = q.popleft()

                if node.left:
                    q.append((node.left, (end << 1)))
                if node.right:
                    q.append((node.right, ((end << 1) + 1)))
                
            ans = max(ans, end-first)

        return ans + 1
    
class Solution:
    firstMap = {}
    maxWidth = 0

    def dfs(self, root: TreeNode, level: int, num: int):
        if root == None:
            return
        
        if level not in self.firstMap:
            self.firstMap[level] = num
        
        self.maxWidth = max(self.maxWidth, num - self.firstMap[level])

        self.dfs(root.left, level+1, num << 1)
        self.dfs(root.right, level+1, ((num << 1) +1))

    def widthOfBinaryTree(self, root: TreeNode) -> int:

        self.firstMap = {}
        self.maxWidth = 0
        self.dfs(root, 0, 0)

        return self.maxWidth + 1





        
