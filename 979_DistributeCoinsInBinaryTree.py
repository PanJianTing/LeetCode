class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def distributeCoins(self, root: TreeNode) -> int:
        self.move = 0

        def dfs(cur):
            if cur == None:
                return 0

            left_coin = dfs(cur.left)
            right_coin = dfs(cur.right)
            self.move += abs(cur.val - 1)
            return (cur.val - 1) + left_coin + right_coin
        
        dfs(root)
        
    def distributeCoins(self, root: TreeNode, pre = None) -> int:
        if root == None:
            return 0
        res = self.distributeCoins(root.left, root) + self.distributeCoins(root.right, root)
        if pre:
            pre.val += root.val - 1
        return res + abs(root.val - 1)