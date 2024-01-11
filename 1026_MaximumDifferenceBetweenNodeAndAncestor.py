class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxAncestorDiff(self, root) -> int:
        if root == None:
            return 0
        
        def dfs(cur, min_val, max_val):
            if cur == None:
                return abs(max_val - min_val)
            max_val = max(cur.val, max_val)
            min_val = min(cur.val, min_val)
            return max(dfs(cur.left, min_val, max_val), dfs(cur.right, min_val, max_val))

        return dfs(root, root.val, root.val)