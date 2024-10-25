from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        def dfs(cur1, cur2):
            if cur1 == None and cur2 == None:
                return True
            
            if cur1 == None and cur2:
                return False
            
            if cur1 and cur2 == None:
                return False
            
            if cur1.val != cur2.val:
                return False
            
            swap = dfs(cur1.left, cur2.right) & dfs(cur1.right, cur2.left)
            no_swap = dfs(cur1.left, cur2.left) & dfs(cur1.right, cur2.right)

            return swap | no_swap


        return dfs(root1, root2)
    

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        st = []
        st.append((root1, root2))


        def is_equal(cur1, cur2):
            if cur1 == None and cur2 == None:
                return True
            if cur1 and cur2 and cur1.val == cur2.val:
                return True
            return False
        
        while st:
            node1, node2 = st.pop()

            if node1 == None and node2 == None:
                continue
            if node1 and node2 == None:
                return False
            if node1 == None and node2:
                return False
            if node1.val != node2.val:
                return False
            
            
            if is_equal(node1.left, node2.left) and is_equal(node1.right, node2.right):
                st.append((node1.left, node2.left))
                st.append((node1.right, node2.right))
            elif is_equal(node1.left, node2.right) and is_equal(node1.right, node2.left):
                st.append((node1.left, node2.right))
                st.append((node1.right, node2.left))
            else:
                return False
            
        return True
        
    

node1_1 = TreeNode(1)
node1_2 = TreeNode(2)
node1_3 = TreeNode(3)
node1_4 = TreeNode(4)
node1_5 = TreeNode(5)
node1_6 = TreeNode(6)
node1_7 = TreeNode(7)
node1_8 = TreeNode(8)

node1_1.left = node1_2
node1_1.right = node1_3

node1_3.left = node1_6

node1_2.left = node1_4
node1_2.right = node1_5

node1_5.left = node1_7
node1_5.right = node1_8



node2_1 = TreeNode(1)
node2_2 = TreeNode(2)
node2_3 = TreeNode(3)
node2_4 = TreeNode(4)
node2_5 = TreeNode(5)
node2_6 = TreeNode(6)
node2_7 = TreeNode(7)
node2_8 = TreeNode(8)

node2_1.left = node2_3
node2_1.right = node2_2

node2_3.right = node2_6


node2_2.left = node2_4
node2_2.right = node2_5


node2_5.left = node2_8
node2_5.right = node2_7

print(Solution().flipEquiv(node1_1, node2_1))

                

