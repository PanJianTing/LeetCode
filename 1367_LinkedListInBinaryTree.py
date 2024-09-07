class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val= 0, left= None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        if root == None:
            return False
        
        def dfs(cur_head, cur_node) -> bool:
            if cur_head == None:
                return True
            if cur_node == None:
                return False
            
            if cur_head.val == cur_node.val:
                return dfs(cur_head.next, cur_node.left) or dfs(cur_head.next, cur_node.right)

            return False
        
        if dfs(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        st = []
        st.append(root)

        def is_match(cur):
            cur_st = []
            cur_st = [(cur, head)]

            while cur_st:
                node, cur_head = cur_st.pop()
                
                while node and cur_head:
                    if node.val != cur_head.val:
                        break
                    cur_head = cur_head.next
                    if cur_head:
                        if node.left:
                            cur_st.append((node.left, cur_head))
                        if node.right:
                            cur_st.append((node.right, cur_head))
                        break
                
                if cur_head == None:
                    return True
            return False

        while st:
            cur = st.pop()

            if is_match(cur):
                return True

            if cur.left:
                st.append(cur.left)
            
            if cur.right:
                st.append(cur.right)
        
        return False

            

    


node1 = TreeNode(1)
node2 = TreeNode(1)
node3 = TreeNode(10)
node4 = TreeNode(1)
node5 = TreeNode(9)

node1.right = node2

node2.left = node3
node2.right = node4


node3.left = node5


list_node1 = ListNode(1)
list_node10 = ListNode(10)


list_node1.next = list_node10

print(Solution().isSubPath(list_node1, node1))

    
