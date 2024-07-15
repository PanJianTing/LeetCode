from collections import defaultdict
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
 

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:

        parent_map = defaultdict(list)
        parent_set = set()

        for p, c, l in descriptions:
            parent_map[p].append((c, l))
            parent_set.add(p)
        
        for p, c, l in descriptions:
            if c in parent_set:
                parent_set.remove(c)
        
        root = list(parent_set)[0]
        root = TreeNode(list(parent_set)[0])
        q = deque()

        q.append(root)

        while q:
            cur_node = q.popleft()
            if cur_node.val in parent_map:
                for c, l in parent_map[cur_node.val]:
                    if l:
                        cur_node.left = TreeNode(c)
                        q.append(cur_node.left)
                    else:
                        cur_node.right = TreeNode(c)
                        q.append(cur_node.right)
        return root
    
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        node_map = defaultdict(list)
        child = set()
        allNode = set()

        for p, c, l in descriptions:
            node_map[p].append((c, l))
            allNode.add(p)
            allNode.add(c)
            child.add(c)
        
        root = 0
        for node in allNode:
            if node not in child:
                root = node
                break
        
        def dfs(cur):
            if cur == None:
                return
            node = TreeNode(cur)

            if cur in node_map:
                for c, l in node_map[cur]:
                    if l:
                        node.left = dfs(c)
                    else:
                        node.right = dfs(c)
            return node

        return dfs(root)
    
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        node_map = defaultdict(TreeNode)
        child_set = set()

        for p, c, l in descriptions:
            if p not in node_map:
                node_map[p] = TreeNode(p)
            if c not in node_map:
                node_map[c] = TreeNode(c)
            
            if l:
                node_map[p].left = node_map[c]
            else:
                node_map[p].right = node_map[c]
            
            child_set.add(c)

        for k in node_map.keys():
            if k not in child_set:
                return node_map[k]
        
        return None


        
print(Solution().createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))  