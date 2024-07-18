from collections import defaultdict
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        adj = defaultdict(list)
        leafs = []
        res = 0

        def getGraph(cur):
            if cur == None:
                return None
            
            if cur.left == None and cur.right == None:
                leafs.append(cur)
            
            if cur.left:
                adj[cur].append(cur.left)
                adj[cur.left].append(cur)
            if cur.right:
                adj[cur].append(cur.right)
                adj[cur.right].append(cur)
            getGraph(cur.left)
            getGraph(cur.right)
            return
        
        getGraph(root)
        
        for st_node in leafs:
            q = deque()
            q.append((st_node, 0))
            other_leafs = set(leafs)
            other_leafs.remove(st_node)
            visit = set()
            visit.add(st_node)

            while q:
                cur_node, cur_dis = q.popleft()
                
                if cur_dis > distance:
                    continue

                if cur_node in other_leafs:
                    res += 1

                visit.add(cur_node)
                
                for next_node in adj[cur_node]:
                    if next_node not in visit:
                        q.append((next_node, cur_dis+1))
        return res >> 1
    

    def countPairs(self, root: TreeNode, distance: int) -> int:

        def postOrder(cur):
            if cur == None:
                return [0] * 12
            if cur.left == None and cur.right == None:
                res = [0] * 12
                res[0] = 1
                return res

            left = postOrder(cur.left)
            right = postOrder(cur.right)

            cur_cnt = [0] * 12

            for i in range(10):
                cur_cnt[i+1] = left[i] + right[i]
            
            cur_cnt[11] = left[11] + right[11]

            for d1 in range(distance+1):
                for d2 in range(distance+1):
                    if 2 + d1 + d2 <= distance:
                        cur_cnt[11] += (left[d1] * right[d2])

            return cur_cnt
        
        return postOrder(root)[11]

        
node15 = TreeNode(15)
node66 = TreeNode(66)
node55 = TreeNode(55)
node97 = TreeNode(97)
node60 = TreeNode(60)
node12 = TreeNode(12)
node56 = TreeNode(56)
node54 = TreeNode(54)
node49 = TreeNode(49)
node9 = TreeNode(9)
node90 = TreeNode(90)


node15.left = node66
node15.right = node55

node66.left = node97
node66.right = node60

node55.left = node12
node55.right = node56

node97.right = node54

node60.right = node49
node49.right = node90

node12.right = node9


print(Solution().countPairs(node15, 5))
            