class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: [TreeNode], root2: [TreeNode]) -> bool:

        leaf1 = []
        leaf2 = []

        def getLeaf(root):
            st = []
            cur = root
            res = []
            while cur or st:
                if cur:
                    st.append(cur)
                    cur = cur.left
                else:
                    p = st.pop()
                    if p.left == None and p.right == None:
                        res.append(p.val)
                    if p.right:
                        cur = p.right
            return res
        
        leaf1 = getLeaf(root1)
        leaf2 = getLeaf(root2)

        return leaf1 == leaf2
    
    def leafSimilar(self, root1, root2) -> bool:

        def dfs(root):
            if root:
                if root.left == None and root.right == None:
                    yield root.val
                yield from dfs(root.left)
                yield from dfs(root.right)
        
        return list(dfs(root1)) == list(dfs(root2))

    

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

node3.left = node5
node3.right = node1

node5.left = node6
node5.right = node2

node1.left = node9
node1.right = node8

node2.left = node7
node2.right = node4


node1_1 = TreeNode(1)
node2_1 = TreeNode(2)
node3_1 = TreeNode(3)
node4_1 = TreeNode(4)
node5_1 = TreeNode(5)
node6_1 = TreeNode(6)
node7_1 = TreeNode(7)
node8_1 = TreeNode(8)
node9_1 = TreeNode(9)

node3_1.left = node5_1
node3_1.right = node1_1

node5_1.left = node6_1
node5_1.right = node7_1

node1_1.left = node4_1
node1_1.right = node2_1

node2_1.left = node9_1
node2_1.right = node8_1

print(Solution().leafSimilar(node3, node3_1))

