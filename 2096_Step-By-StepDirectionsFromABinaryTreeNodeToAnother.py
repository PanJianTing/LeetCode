from collections import defaultdict
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        direction_map = {}
        
        def getDirection(cur):
            q = deque()
            q.append(cur)

            adj = defaultdict(list)

            while q:
                cur_node = q.popleft()

                if cur_node.left:
                    adj[cur_node.val].append((cur_node.left.val, 'L'))
                    adj[cur_node.left.val].append((cur_node.val, 'U'))
                    q.append(cur_node.left)
                
                if cur_node.right:
                    adj[cur_node.val].append((cur_node.right.val, 'R'))
                    adj[cur_node.right.val].append((cur_node.val, 'U'))
                    q.append(cur_node.right)

            return adj

        direction_map = getDirection(root)
        q = deque()
        q.append((startValue, ""))
        visit = set()
        visit.add(startValue)

        while q:
            cur_val, cur_path = q.popleft()
            
            if cur_val == destValue:
                return cur_path

            for next_val, next_dir in direction_map[cur_val]:
                if next_val not in visit:
                    next_path = cur_path + next_dir
                    q.append((next_val, next_path))
                    visit.add(next_val)
        
        return ""
    

    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:

        parent_map = defaultdict(TreeNode)
        pathTrack = {}

        def findStartNode(cur):
            if cur == None:
                return None
            if cur.val == startValue:
                return cur

            left_node = findStartNode(cur.left)
            if left_node:
                return left_node
            return findStartNode(cur.right)
        
        def pop_parent_map(cur):
            if cur == None:
                return
            if cur.left:
                parent_map[cur.left.val] = cur
                pop_parent_map(cur.left)
            if cur.right:
                parent_map[cur.right.val] = cur
                pop_parent_map(cur.right)
            
            return
        
        def backtractNode(cur):

            path = []
            while cur in pathTrack:
                node, direction = pathTrack[cur]
                path.append(direction)
                cur = node
            path = path[::-1]
            return "".join(path)

        
        start_node = findStartNode(root)
        pop_parent_map(root)

        q = deque()
        q.append(start_node)
        visit = set()
        visit.add(start_node)

        while q:
            cur_node = q.popleft()
            
            if cur_node.val == destValue:
                return backtractNode(cur_node)

            if cur_node.val in parent_map:
                parent_node = parent_map[cur_node.val]
                if parent_node not in visit:
                    q.append(parent_node)
                    pathTrack[parent_node] = (cur_node, "U")
                    visit.add(parent_node)

            if cur_node.left and cur_node.left not in visit:
                q.append(cur_node.left)
                pathTrack[cur_node.left] = (cur_node, "L")
                visit.add(cur_node.left)
            
            if cur_node.right and cur_node.right not in visit:
                q.append(cur_node.right)
                pathTrack[cur_node.right] = (cur_node, "R")
                visit.add(cur_node.right)
        
        return ""
    

    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:

        def findLowestCommonAncestor(node):
            if node == None:
                return None
            
            if node.val == startValue or node.val == destValue:
                return node
            
            left_lca = findLowestCommonAncestor(node.left)
            right_lca = findLowestCommonAncestor(node.right)

            if left_lca == None:
                return right_lca
            if right_lca == None:
                return left_lca
            return node
        
        def findPath(node, target, path):
            if node == None:
                return False
            
            if node.val == target:
                return True
            
            path.append("L")
            left_res = findPath(node.left, target, path)
            
            if left_res:
                return True
            else:
                path.pop()

            path.append("R")
            right_res = findPath(node.right, target, path)
            
            if right_res:
                return True
            else:
                path.pop()
            
            return False
        
        lca = findLowestCommonAncestor(root)
        
        pathToStart = []
        pathtoEnd = []

        findPath(lca, startValue, pathToStart)
        findPath(lca, destValue, pathtoEnd)

        res = ['U' * len(pathToStart)]
        res += pathtoEnd
        
        return "".join(res)
    
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        pathToStart = []
        pathToEnd = []
        idx = 0
        res = []

        def findPath(cur, target, path):
            if cur == None:
                return False
            if cur.val == target:
                return True
            
            path.append("L")
            left_res = findPath(cur.left, target, path)
            if left_res:
                return True
            else:
                path.pop()
            
            path.append("R")
            right_res = findPath(cur.right, target, path)
            if right_res:
                return True
            else:
                path.pop()
            
            return False
        
        findPath(root, startValue, pathToStart)
        findPath(root, destValue, pathToEnd)

        while idx < len(pathToStart) and idx < len(pathToEnd) and pathToStart[idx] == pathToEnd[idx]:
            idx += 1

        res = ["U" * (len(pathToStart) - idx)]
        res += pathToEnd[idx:]

        return ''.join(res)
    
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        
        def find(node, val, path):
            if node.val == val:
                return True
            if node.left and find(node.left, val, path):
                path.append('L')
                return True
            if node.right and find(node.right, val, path):
                path.append('R')
                return True
            return False
        p1 = []
        p2 = []
        find(root, startValue, p1)
        find(root, destValue, p2)
        while p1 and p2 and p1[-1] == p2[-1]:
            p1.pop()
            p2.pop()
        return 'U' * len(p1) + ''.join(p2[::-1])


        


                
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)


node5.left = node1
node5.right = node2

node1.left = node3

node2.left = node6
node2.right = node4

print(Solution().getDirections(node5, 3, 6))



                

