from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root: Optional[TreeNode], leafList: list[int]) -> list[int]:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if not curr.left and not curr.right:
                leafList.append(curr.val)
            curr = curr.right


    def travelTree(self, root: Optional[TreeNode], leafList: list[int]) -> list[int]:

        if root == None:
            return leafList
        elif root.right == None and root.left == None:
            leafList.append(root.val)
            return leafList
        else:
            self.travelTree(root.left, leafList)
            self.travelTree(root.right, leafList)



    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leaf1 = []
        leaf2 = []

        self.inorder(self, root1, leaf1)
        self.inorder(self, root2, leaf2)

        return leaf1 == leaf2



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

node1.left = node9
node1.right = node8

node2.left = node7
node2.right = node4

node3.left = node5
node3.right = node1

node5.left = node6
node5.right = node2


Solution.leafSimilar(Solution, node3, node3)
