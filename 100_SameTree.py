from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_queue = deque()
        q_queue = deque()
        p_queue.append(p)
        q_queue.append(q)

        while p_queue and q_queue:
            cur_p = p_queue.popleft()
            cur_q = q_queue.popleft()
            
            if cur_p and cur_q == None:
                return False
            if cur_p == None and cur_q:
                return False
            if cur_p and cur_q and cur_p.val != cur_q.val:
                return False
            
            if cur_p:
                p_queue.append(cur_p.left)
                p_queue.append(cur_p.right)
            if cur_q:
                q_queue.append(cur_q.left)
                q_queue.append(cur_q.right)
        return p_queue == q_queue
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)
        else:
            return False
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        my_q = deque()

        my_q.append((p,q))

        while my_q:
            cur_p, cur_q = my_q.popleft()
            
            if cur_p == None and cur_q == None:
                continue
            if cur_p == None or cur_q == None:
                return False
            if cur_p.val != cur_q.val:
                return False

            my_q.append((cur_p.left, cur_q.left))
            my_q.append((cur_p.right, cur_q.right))
        return True