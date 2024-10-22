from collections import defaultdict, deque
import heapq

class TreeNode:
    def __init__(self, val= 0, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        level_map = defaultdict(int)

        def dfs(cur, level):
            if cur == None:
                return
            level_map[level] += cur.val
            dfs(cur.left, level + 1)
            dfs(cur.right, level + 1)
            return
        
        dfs(root, 0)
        sum_list = sorted(level_map.values(), reverse=True)
        return sum_list[k-1] if len(sum_list) > k-1 else -1
    
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        hq = []
        q = deque()
        q.append(root)

        while q:
            N = len(q)
            level_sum = 0

            for _ in range(N):
                cur_node = q.popleft()
                level_sum += cur_node.val
                
                if cur_node.left:
                    q.append(cur_node.left)
                
                if cur_node.right:
                    q.append(cur_node.right)
            heapq.heappush(hq, -1 * level_sum)
        
        if len(hq) < k:
            return -1
        
        for _ in range(k-1):
            heapq.heappop(hq)
        
        return hq[0] * -1
    

    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        hq = []
        q = deque()
        q.append(root)

        while q:
            N = len(q)
            level_sum = 0

            for _ in range(N):
                cur_node = q.popleft()
                level_sum += cur_node.val
                
                if cur_node.left:
                    q.append(cur_node.left)
                
                if cur_node.right:
                    q.append(cur_node.right)    
            heapq.heappush(hq, level_sum)
            if len(hq) > k:
                heapq.heappop(hq)
        
        if len(hq) < k:
            return -1
        
        return hq[0]



