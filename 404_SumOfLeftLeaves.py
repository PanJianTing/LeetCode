class Solution:
    def sumLeft(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return root.val
        else:
            allSum = self.sumLeft(root.left) + self.sumLeft(root.right)
            if root.right:
                if root.right.left == None and root.right.right == None:
                    allSum -= root.right.val
            return  allSum


    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if root.left == None and root.right == None:
            return 0
        return self.sumLeft(root)


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        sumLeft = 0
        if root.left != None and root.left.left == None and root.left.right == None:
            sumLeft = root.left.val
        return sumLeft + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right