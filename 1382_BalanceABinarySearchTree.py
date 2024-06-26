class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        val_list = []

        def inorder(cur):
            if cur == None:
                return
            
            inorder(cur.left)
            val_list.append(cur.val)
            inorder(cur.right)
        
        def buildTree(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(val_list[l])

            mid = l + ((r-l) >> 1)
            cur = TreeNode(val_list[mid])
            cur.left = buildTree(l, mid-1)
            cur.right = buildTree(mid+1, r)
            return cur
        
        inorder(root)
        return buildTree(0, len(val_list)-1)
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        val_list = []
        st = []
        cur = root
        while st or cur:
            while cur:
                st.append(cur)
                cur = cur.left
            

            cur = st.pop()
            val_list.append(cur.val)
            cur = cur.right


        def buildTree(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(val_list[l])
            
            m = l + ((r-l) >> 1)
            cur = TreeNode(val_list[m], buildTree(l, m-1), buildTree(m+1, r))
            return cur

        return buildTree(0, len(val_list) - 1)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node3.left = node1
node3.right = node4

node1.right = node2






print(Solution().balanceBST(node3))