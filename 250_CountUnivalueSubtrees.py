class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    count = 0
    def dfs(self, root) -> bool:
        if root == None:
            return True
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left and right:
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False
            self.count += 1
            return True
        return False
    
    def dfs(self, root) -> tuple:
        if root == None:
            return (True, 0)

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        count = left[1] + right[1]

        if left[0] and left[0]:
            if root.left and root.left.val != root.val:
                return (False, count)
            if root.right and root.right.val != root.val:
                return (False, count)
            
            count += 1
            return (True, count)
        
        return (False, count)

    def countUnivalSubtrees(self, root) ->int:
        self.count = 0
        self.dfs(root)
        return self.count
    
class Solution:
    
    def dfs(self, root) -> tuple:
        if root == None:
            return (True, 0)

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        count = left[1] + right[1]

        if left[0] and left[0]:
            if root.left and root.left.val != root.val:
                return (False, count)
            if root.right and root.right.val != root.val:
                return (False, count)
            
            count += 1
            return (True, count)
        
        return (False, count)

    def countUnivalSubtrees(self, root) ->int:

        return self.dfs(root)[1]


node1 = TreeNode(5)
node2 = TreeNode(5)
node3 = TreeNode(5)
node4 = TreeNode(5)
node5 = TreeNode(5)
node6 = TreeNode(5)

node1.left = node2
node1.right = node3


node2.left = node4
node2.right = node5

node3.right = node6

print(Solution().countUnivalSubtrees(node1))