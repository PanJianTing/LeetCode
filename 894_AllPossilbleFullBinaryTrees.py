class TreeNode:
    def __init__(self, val= 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n) -> list[TreeNode]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]
        
        res = []
        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n-i-1)

            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    res.append(root)

        return res
    

    def allPossibleFBT(self, n) -> list[TreeNode]:

        if n % 2 == 0:
            return []
        
        dp = [[] for _ in range(n+1)]

        dp[1].append(TreeNode())

        for cnt in range(3, n+1, 2):
            for i in range(1, cnt, 2):
                j = cnt - i - 1
                for l in dp[i]:
                    for r in dp[j]:
                        root = TreeNode(0, l, r)
                        dp[cnt].append(root)

        return dp[n]
    

Solution().allPossibleFBT(7)
