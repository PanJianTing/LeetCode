class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxD(self, root: TreeNode, depth: int) -> int:
        
        if root == None:
            return depth

        depth += 1

        return max(depth, self.maxD(root.left, depth), self.maxD(root.right, depth))

    def maxDepth(self, root: TreeNode) -> int:

        return self.maxD(root, 0)

    
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root: TreeNode) -> int:

        stack = []
        if root is not None:
            stack.append((root, 1))

        depth = 0

        while stack != []:
            node, currentDepth = stack.pop()
            if node != None:
                depth = max(depth, currentDepth)
                stack.append((node.left, currentDepth + 1))
                stack.append((node.right, currentDepth + 1))

        return depth


