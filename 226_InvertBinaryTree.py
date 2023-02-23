from collections import deque

class TreeNode:
    def __init__(self, val= 0, left= None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        q = deque()

        q.append(root)

        while len(q) > 0:
            node = q.popleft()
            if node != None:
                node.left, node.right = node.right, node.left
                q.append(node.right)
                q.append(node.left)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:

        if root == None:
            return root

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root


node4 = TreeNode(4)
node2 = TreeNode(4)
node7 = TreeNode(4)
node1 = TreeNode(4)
node3 = TreeNode(4)
node6 = TreeNode(4)
node9 = TreeNode(4)

node4.left = node2
node4.right = node7

node2.left = node1
node2.right = node3

node7.left = node6
node7.right = node9


Solution().invertTree(node4)
        


