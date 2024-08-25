class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        self.res = []

        def postorder(cur):
            if cur == None:
                return
            
            postorder(cur.left)
            postorder(cur.right)
            self.res.append(cur.val)
        postorder(root)
        return self.res
    
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        st = []
        cur = root

        while cur or st:
            if cur:
                res.append(cur.val)
                st.append(cur)
                cur = cur.right
            else:
                cur = st.pop()
                cur = cur.left
        res.reverse()
        return res

