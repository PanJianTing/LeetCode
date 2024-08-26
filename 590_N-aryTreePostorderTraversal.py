class Node:
    def __init__(self, val = None, children = []):
        self.val = val
        self.children = children
        

class Solution:


    def postorder(self, root: Node) -> list[int]:
        self.res = []
        def traversal(cur):
            if cur == None:
                return
            
            for child in cur.children:
                traversal(child)
            
            self.res.append(cur.val)
        
        traversal(root)
        return self.res

    def postorder(self, root: Node) -> list[int]:
        if root == None:
            return []
        
        res = []
        st = []
        st.append(root)

        while st:
            cur = st.pop()
            res.append(cur.val)
            
            for child in cur.children:
                st.append(child)
        res.reverse()
        return res
    
    def postorder(self, root: Node) -> list[int]:
        res = []

        def traversal(cur, res):
            if cur == None:
                return 

            for child in cur.children:
                traversal(child, res)
            
            res.append(cur.val)
        
        traversal(root, res)
        return res
    

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.children = [node3, node2, node4]
node3.children = [node5, node6]

print(Solution().postorder(node1))