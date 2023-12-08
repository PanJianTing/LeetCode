class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def __init__(self) -> None:
    #     self.ans = 0
    
    def maximumAverageSubtree(self, root) -> float:
        if root == None:
            return 0.0
        
        self.ans = 0
        
        def dp(cur) -> (int, int):
            if cur == None:
                return (0, 0)

            leftSum, leftCnt = (0, 0)
            rightSum, rightCnt = (0, 0)

            if cur.left:
                leftSum, leftCnt = dp(cur.left)

            if cur.right:
                rightSum, rightCnt = dp(cur.right)

            total = cur.val + leftSum + rightSum
            cnt = 1 + leftCnt + rightCnt
            self.ans = max(self.ans, total / cnt)
            return (total, cnt)
        dp(root)
        return self.ans
        
node5 = TreeNode(5)
node6 = TreeNode(6)
node1 = TreeNode(1)

node5.left = node6
node5.right = node1

print(Solution().maximumAverageSubtree(node5))

node0 = TreeNode(0)
node1 = TreeNode(1)

node0.right = node1
print(Solution().maximumAverageSubtree(node0))