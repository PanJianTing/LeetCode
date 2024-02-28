from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        ans = root.val
        while q:
            N = len(q)
            ans = q[0].val

            for _ in range(N):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return ans
    
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        ans = root
        
        while q:
            cur = q.popleft()
            ans = cur
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
        return ans.val
    

    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.ans = (root.val, 0)

        
        def dfs(cur, cur_h):
            if cur == None:
                return
            if cur_h > self.ans[1]:
                self.ans = (cur.val, cur_h)
                
            dfs(cur.left, cur_h+1)
            dfs(cur.right, cur_h+1)
        dfs(root, 0)
        return self.ans[0]

