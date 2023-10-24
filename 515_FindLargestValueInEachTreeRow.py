from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        
        ans = []
        q = deque()
        q.append(root)

        while q:
            N = len(q)
            max_val = float('-inf')

            for _ in range(N):
                cur = q.popleft()
                max_val = max(cur.val, max_val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
            ans.append(max_val)
        return ans
    

    def largestValues(self, root) -> list[int]:

        ans = []

        def dp(root, d):
            if root == None:
                return
            
            if d >= len(ans):
                ans.append(root.val)
            else:
                ans[d] = max(ans[d], root.val)
            
            dp(root.left, d+1)
            dp(root.right, d+1)
        
        dp(root, 0)
        return ans
    
    def largestValues(self, root):
        if root == None:
            return []
        
        ans = []
        st = []
        st.append((root, 0))

        while st:
            cur, d = st.pop()

            if d >= len(ans):
                ans.append(cur.val)
            else:
                ans[d] = max(cur.val, ans[d])
            
            if cur.left:
                st.append((cur.left, d+1))
            if cur.right:
                st.append((cur.right, d+1))
        
        return ans
    

    def largestValues(self, root):
        ans = []
        row = [root]

        while any(row):
            ans.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return ans