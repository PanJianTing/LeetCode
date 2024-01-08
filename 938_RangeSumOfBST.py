from collections import deque
from collections import defaultdict

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        q = deque()
        q.append(root)
        ans = 0

        while q:
            cur = q.popleft()
            if low <= cur.val <= high:
                ans += cur.val
            if cur.left and cur.val > low:
                q.append(cur.left)
            if cur.right and cur.val < high:
                q.append(cur.right)

        return ans
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def dfs(cur):
            ans = 0
            if low <= cur.val <= high:
                ans += cur.val
            
            if cur.left and cur.val > low:
                ans += dfs(cur.left)
            
            if cur.right and cur.val < high:
                ans += dfs(cur.right)
            
            return ans

        return dfs(root)



    

node3 = TreeNode(3)
node5 = TreeNode(5)
node7 = TreeNode(7)
node10 = TreeNode(10)
node15 = TreeNode(15)
node18 = TreeNode(18)


node10.left = node5
node10.right = node15

node5.left = node3
node5.right = node7

node15.right = node18

print(Solution().rangeSumBST(node10, 7, 15))