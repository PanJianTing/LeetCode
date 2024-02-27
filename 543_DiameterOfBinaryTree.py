from functools import cache

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        @cache
        def getHeight(cur):
            if cur == None:
                return 0
            return 1 + max(getHeight(cur.left), getHeight(cur.right))
        
        @cache
        def getDiameter(cur):
            if cur == None:
                return 0
            cur_diameter = getHeight(cur.left) + getHeight(cur.right)
            return max(cur_diameter, getDiameter(cur.left), getDiameter(cur.right))
        return getDiameter(root)
    

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def dfs(cur):
            if cur == None:
                return 0
            left_h =  dfs(cur.left)
            right_h = dfs(cur.right)
            self.diameter = max(self.diameter, left_h + right_h)
            return 1 + max(left_h, right_h)
        dfs(root)
        return self.diameter
