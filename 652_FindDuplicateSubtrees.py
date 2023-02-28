from collections import defaultdict

class TreeNode:
    def __init__(self, val= 0, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def traverse(self, node: TreeNode, cnt: dict, res: list[TreeNode]) -> str:

        if node == None:
            return ""
        
        representation = "(" + self.traverse(node.left, cnt, res) + ")" + str(node.val) + "(" + self.traverse(node.right, cnt, res) + ")"
        print(representation)
        cnt[representation] += 1


        if cnt[representation] == 2:
            res.append(node)
        return representation
    
    def traverse(self, node: TreeNode, tripletToId: dict, cnt: dict, res: list[TreeNode]) -> int:

        if node == None:
            return 0
        
        triplet = (self.traverse(node.left, tripletToId, cnt, res), node.val, self.traverse(node.right, tripletToId, cnt, res))

        print(triplet)
        if triplet not in tripletToId:
            tripletToId[triplet] = len(tripletToId) + 1
        id = tripletToId[triplet]
        cnt[id] += 1
        if cnt[id] == 2:
            res.append(node)
        return id


    
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:
        res = list()
        cnt = defaultdict(int)
        tripletToId = dict()
        # self.traverse(root, cnt, res)
        self.traverse(root, tripletToId, cnt, res)
        return res
    
    def trv(self, node: TreeNode, nodes: dict) -> str:

        if not node: 
            return "null"
        struct = "%s,%s,%s" % (self.trv(node.left, nodes), str(node.val), self.trv(node.right, nodes))
        nodes[struct].append(node)
        return struct


    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:

        nodes = defaultdict(list)
        self.trv(root, nodes)

        # print(nodes)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]


        
    

node1 = TreeNode(1)
node21 = TreeNode(2)
node22 = TreeNode(2)
node3 = TreeNode(3)
node41 = TreeNode(5)
node42 = TreeNode(4)
node43 = TreeNode(4)

node1.left = node21
node1.right = node3

node21.left = node41

node3.left = node22
node3.right = node42

node22.left = node43

print(Solution().findDuplicateSubtrees(node1))