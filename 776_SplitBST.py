class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def splitBST(self, root: TreeNode, target: int) -> list[TreeNode]:
        
        if root == None:
            return [None, None]
        
        if root.val > target:
            res = self.splitBST(root.left, target)
            root.left = res[1]

            return [res[0], root]
        
        res = self.splitBST(root.right, target)
        root.right = res[0]
        return [root, res[1]]
    
    def splitBST(self, root: TreeNode, target: int) -> list[TreeNode]:
        ans = [None, None]
        
        if root == None:
            return ans
        
        st = []

        while root:
            st.append(root)
            if root.val > target:
                root = root.left
            else:
                root = root.right
        
        while st:
            cur = st.pop()
            if cur.val > target:
                cur.left = ans[1]
                ans[1] = cur
            else:
                cur.right = ans[0]
                ans[0] = cur
        
        return ans
    
    def splitBST(self, root: TreeNode, target: int) -> list[TreeNode]:

        dummyS = TreeNode(0)
        dummyL = TreeNode(0)

        curSmall = dummyS
        curLarge = dummyL

        cur = root
        nextNode = None

        while cur:
            if cur.val <= target:
                curSmall.right = cur
                curSmall = cur

                nextNode = cur.right
                curSmall.right = None
                cur = nextNode
            else:
                curLarge.left = cur
                curLarge = cur
                
                nextNode = cur.left
                curLarge.left = None
                cur = nextNode
        
        return [dummyS.right, dummyL.left]
    

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node4.left = node2
node4.right = node6

node2.left = node1
node2.right = node3

node6.left = node5
node6.right = node7

res = Solution().splitBST(node4, 2)
