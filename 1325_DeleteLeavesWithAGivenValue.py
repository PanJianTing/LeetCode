class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        def dfs(cur):

            if cur.left:
                cur.left = dfs(cur.left)
            if cur.right:
                cur.right = dfs(cur.right)

            if cur.left == None and cur.right == None and cur.val == target:
                return None
            return cur
        
        return dfs(root)
        
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        if root == None:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.left == None and root.right == None and root.val == target:
            return None
        return root
    

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        st = []
        cur = root
        lastRight = None

        while st or cur:
            
            while cur:
                st.append(cur)
                cur = cur.left
            
            cur = st[-1]

            if cur.right != lastRight and cur.right != None:
                cur = cur.right
                continue
            st.pop()

            if cur.right == None and cur.left == None and cur.val == target:
                if len(st) == 0:
                    return None

                parent = st[-1]

                if parent.left == cur:
                    parent.left = None
                if parent.right == cur:
                    parent.right = None
            
            lastRight = cur
            cur = None
        return root
    

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root == None:
            return None
        
        st = [(root, None, False)] # cur, parent, is_left_child
        last = None
        visit = set()
        visit.add(root)

        while st:
            cur, parent, is_left_child = st[-1]

            if cur.left and cur.left != last and cur.left not in visit:
                st.append((cur.left, cur, True))
                visit.add(cur.left)
            elif cur.right and last != cur.right and cur.right not in visit:
                st.append((cur.right, cur, False))
                visit.add(cur.right)
            else:
                st.pop()
                last = cur

                if cur.left == None and cur.right == None and cur.val == target:
                    if parent:
                        if is_left_child:
                            parent.left = None
                        else:
                            parent.right = None
                    else:
                        root = None
        return root


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(2)
node5 = TreeNode(2)
node6 = TreeNode(4)

node1.left = node2
node1.right = node3

# node2.left = node4

# node3.left = node5
# node3.right = node6

Solution().removeLeafNodes(node1, 1)


