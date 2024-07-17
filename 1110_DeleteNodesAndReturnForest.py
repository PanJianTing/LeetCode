from collections import deque
from collections import defaultdict

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        res = set()
        parent_map = defaultdict(TreeNode)
        to_delete = set(to_delete)
        q = deque()
        res.add(root)
        q.append(root)

        while q:
            cur = q.popleft()
            if cur.left:
                parent_map[cur.left] = (cur, "L")
                q.append(cur.left)
            if cur.right:
                parent_map[cur.right] = (cur, "R")
                q.append(cur.right)
        
        q.append(root)

        while q:
            cur = q.popleft()

            if cur.val in to_delete:
                if cur in parent_map:
                    parent_node, direction = parent_map[cur]
                    if direction == "L":
                        parent_node.left = None
                    if direction == "R":
                        parent_node.right = None
                
                if cur in res:
                    res.remove(cur)
                
                if cur.left:
                    res.add(cur.left)
                
                if cur.right: 
                    res.add(cur.right)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        
        return res
    
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        to_delete = set(to_delete)
        res = []
        def dfs(cur):
            if cur == None:
                return None
            
            cur.left = dfs(cur.left)
            cur.right = dfs(cur.right)

            if cur.val in to_delete:
                if cur.left:
                    res.append(cur.left)
                if cur.right:
                    res.append(cur.right)
                
                return None
            return cur
        cur = dfs(root)
        if cur:
            res.append(cur)
        return res
    

    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        to_delete = set(to_delete)
        res = []

        q = deque()
        q.append(root)

        while q:
            cur = q.popleft()

            if cur.left:
                q.append(cur.left)
                if cur.left.val in to_delete:
                    cur.left = None
            
            if cur.right: 
                q.append(cur.right)
                if cur.right.val in to_delete:
                    cur.right = None

            if cur.val in to_delete:
                if cur.left:
                    res.append(cur.left)
                
                if cur.right:
                    res.append(cur.right)

        if root.val not in to_delete:
            res.append(root)

        return res

    


        
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left= node6
node3.right = node7

print(Solution().delNodes(node1, [3,5]))