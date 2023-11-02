class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val

class Solution:
    ans = 0
    def averageOfSubtree(self, root: TreeNode) -> int:

        self.ans = 0

        def dp(root):

            if root == None:
                return (0, 0)

            leftSum, leftCnt = dp(root.left)
            rightSum, rightCnt = dp(root.right)

            totalSum = root.val + leftSum + rightSum
            totalCnt = 1 + leftCnt + rightCnt

            if root.val == (totalSum // totalCnt):
                self.ans += 1
            return (totalSum, totalCnt)
        dp(root)
        return self.ans