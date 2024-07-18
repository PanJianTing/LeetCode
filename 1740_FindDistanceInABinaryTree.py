from collections import deque

class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        p_path = []
        q_path = []

        def distance(cur, target, path):
            if cur == None:
                return False
            if cur.val == target:
                return True
            
            path.append("L")
            if distance(cur.left, target, path):
                return True
            else:
                path.pop()
            
            path.append("R")
            if distance(cur.right, target, path):
                return True
            else:
                path.pop()
            
            return False
        distance(root, p, p_path)
        distance(root, q, q_path)

        while len(p_path) > 0 and len(q_path) > 0:
            if p_path[0] == q_path[0]:
                p_path.pop(0)
                q_path.pop(0)
            else:
                break
        return len(p_path) + len(q_path)
    

    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        
        def findLCA(cur):
            if cur == None:
                return None
            
            if cur.val == p or cur.val == q:
                return cur
            
            left = findLCA(cur.left)
            right = findLCA(cur.right)
            if left and right:
                return cur
            if left:
                return left
            return right

        def depth(cur, target, deep):
            if cur == None:
                return 0
            
            if cur.val == target:
                return deep
            return max(depth(cur.left, target, deep+1), depth(cur.right, target, deep + 1))

        lca_node = findLCA(root)
        return depth(lca_node, p, 0) + depth(lca_node, q, 0)
    

    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        
        def findLCA(cur):
            if cur == None:
                return None
            
            if cur.val == p or cur.val == q:
                return cur
            
            left = findLCA(cur.left)
            right = findLCA(cur.right)
            if left and right:
                return cur
            if left:
                return left
            return right

        lca_node = findLCA(root)
        qu = deque()
        qu.append((lca_node, 0))
        find_p = False
        find_q = False
        res = 0

        while qu and not (find_p == True and find_q == True):
            cur_node, cur_depth = qu.popleft()

            if cur_node.val == p:
                res += cur_depth
                find_p = True
            if cur_node.val == q:
                res += cur_depth
                find_q = True

            if cur_node.left:
                qu.append((cur_node.left, cur_depth + 1))
            
            if cur_node.right:
                qu.append((cur_node.right, cur_depth + 1))
        
        return res


    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        
        def findLCA(cur, depth):
            if cur == None or p == q:
                return 0
            
            if cur.val == p or cur.val == q:
                left_dis = findLCA(cur.left, 1)
                right_dis = findLCA(cur.right, 1)
                return max(left_dis, right_dis) if left_dis > 0 or right_dis > 0 else depth
            
            left_dis = findLCA(cur.left, depth+1)
            right_dis = findLCA(cur.right, depth+1)
            res = left_dis + right_dis

            if left_dis != 0 and right_dis != 0:
                res -= (depth << 1)
            return res

        
        return findLCA(root, 0)
    

node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node3.left = node5
node3.right = node1

node5.left = node6
node5.right = node2

node2.left = node7
node2.right = node4

node1.left = node0
node1.right = node8

print(Solution().findDistance(node3, 5, 7))
    

