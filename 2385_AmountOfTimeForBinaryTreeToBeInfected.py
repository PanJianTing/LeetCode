from collections import defaultdict
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        
        adj_map = defaultdict(list)
        q = deque()
        q.append(root)
        total_cnt = 0

        while q:
            cur = q.popleft()
            total_cnt += 1
            
            if cur.left:
                adj_map[cur.val].append(cur.left.val)
                adj_map[cur.left.val].append(cur.val)
                q.append(cur.left)
            
            if cur.right:
                adj_map[cur.val].append(cur.right.val)
                adj_map[cur.right.val].append(cur.val)
                q.append(cur.right)
            
        visit = set()
        visit.add(start)
        ans = 0
        q = deque()
        q.append(start)
        
        while q:
            if total_cnt == len(visit):
                return ans
            
            level_cnt = len(q)
            for _ in range(level_cnt):
                cur = q.popleft()

                for num in adj_map[cur]:
                    if num not in visit:
                        q.append(num)
                        visit.add(num)
            ans += 1
        return ans


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node9 = TreeNode(9)
node10 = TreeNode(10)


node1.left = node5
node1.right = node3

node5.right = node4

node3.left = node10
node3.right = node6

node4.left = node9
node4.right = node2

print(Solution().amountOfTime(node1, 3))
            
            

        