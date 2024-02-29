from functools import cache

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def equalToDescendants(self, root: TreeNode) -> int:
        self.cnt = 0
        
        def dfs(cur):
            if cur == None:
                return 0
            
            left_sum = dfs(cur.left)
            right_sum = dfs(cur.right)
            if cur.val == left_sum + right_sum:
                self.cnt += 1
            return cur.val + left_sum + right_sum
        dfs(root)
        return self.cnt