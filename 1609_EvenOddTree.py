from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q = deque()
        q.append(root)
        isEven = True

        while q:
            N = len(q)
            if isEven:
                pre_num = 0
            else:
                pre_num = float('inf')

            for _ in range(N):
                cur_node = q.popleft()
                cur_val = cur_node.val
                if isEven:
                    if not (cur_val % 2 and pre_num < cur_val):
                        return False
                if not isEven:
                    if not (cur_val % 2 == 0 and pre_num > cur_val):
                        return False
                pre_num = cur_val
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            isEven = not isEven

        return True
    
    def isEvenOddTree(self, root: TreeNode) -> bool:
        self.pre = []

        def dfs(cur, level) -> bool:
            if cur == None:
                return True
            
            if cur.val % 2 == level % 2:
                return False
            if len(self.pre) > level:
                if level % 2 and self.pre[level] <= cur.val:
                    return False
                if level % 2 == 0 and self.pre[level] >= cur.val:
                    return False
                self.pre[level] = cur.val
            else:
                self.pre.append(cur.val)
            
            return dfs(cur.left, level+1) and dfs(cur.right, level+1)
        return dfs(root, 0)
    
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q = deque()
        q.append(root)
        isEven = True

        while q:
            N = len(q)
            if isEven:
                pre_num = 0
            else:
                pre_num = float('inf')

            for _ in range(N):
                cur_node = q.popleft()
                cur_val = cur_node.val
                if isEven and (cur_val % 2 == 0 or pre_num >= cur_val):
                        return False
                if not isEven and (cur_val % 2 or pre_num <= cur_val):
                    return False
                pre_num = cur_val
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            isEven = not isEven

        return True
    
        
