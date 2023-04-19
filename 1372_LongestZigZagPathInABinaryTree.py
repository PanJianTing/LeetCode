from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


#bad Solution
class Solution:
    
    def traverse(self, root: TreeNode, isRight: bool) -> int:
        
        if root == None:
            return 0
        if isRight:
            return 1 + self.traverse(root.left, False)
        else:
            return 1 + self.traverse(root.right, True)
    
    def longestZigZag(self, root: TreeNode) -> int:
        ans = 0

        q = deque()

        q.append(root)
        
        while len(q):
            curr = q.popleft()
            tmp = max(self.traverse(curr.left, False), self.traverse(curr.right, True))
            ans = max(ans, tmp)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)


        return ans
    
class Solution:
    res = []
    def traverse(self, root: TreeNode, isRight: bool, len: int):
       self.res.append(len)

       if root:
           if isRight:
               self.traverse(root.left , False, len+1)
               self.traverse(root.right, True, 1)
           else:
               self.traverse(root.right, True, len+1)
               self.traverse(root.left, False, 1)

    def longestZigZag(self, root: TreeNode) -> int:
        self.res = []
        self.traverse(root.right, True, 1)
        self.traverse(root.left, False, 1)

        return max(self.res) - 1
    
class Solution:
    maxLen = 0
    def traverse(self, root: TreeNode, isRight: bool, len: int):

       if root:
           self.maxLen = max(len, self.maxLen)
           if isRight:
               self.traverse(root.left , False, len+1)
               self.traverse(root.right, True, 1)
           else:
               self.traverse(root.left, False, 1)
               self.traverse(root.right, True, len+1)

    def longestZigZag(self, root: TreeNode) -> int:
        self.maxLen = 0
        self.traverse(root, True, 0)
        self.traverse(root, False, 0)

        return self.maxLen


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                return [-1, -1, -1]
            left, right = dfs(root.left), dfs(root.right)
            return [left[1]+1, right[0]+1, max(left[1]+1, right[0]+1, left[2], right[2])]
        return dfs(root)[-1]


        