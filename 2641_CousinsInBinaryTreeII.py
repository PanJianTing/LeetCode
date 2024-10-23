from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        d_sum_map = defaultdict(int)
        node_sum_map = defaultdict(int)

        def dfs(cur, parent, cur_d):
            if cur == None:
                return
            
            d_sum_map[cur_d] += cur.val
            if parent:
                node_sum_map[parent] += cur.val
            dfs(cur.left, cur, cur_d + 1)
            dfs(cur.right, cur, cur_d + 1)

            return
        
        def setVal(cur, parent, cur_d):
            if cur == None:
                return
            
            cousins_sum = 0
            if parent:
                cousins_sum = d_sum_map[cur_d] - node_sum_map[parent]
            cur.val = cousins_sum
            setVal(cur.left, cur, cur_d+1)
            setVal(cur.right, cur, cur_d+1)

        dfs(root, None, 0)
        setVal(root, None, 0)
        return root
    

    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        level_sum_list = []
        q = deque()
        q.append(root)
        
        while q:
            level_cnt = len(q)
            level_sum = 0
            for _ in range(level_cnt):
                cur_node = q.popleft()
                level_sum += cur_node.val

                if cur_node.left:
                    q.append(cur_node.left)
                
                if cur_node.right:
                    q.append(cur_node.right)
            level_sum_list.append(level_sum)
        
        q.append(root)
        cur_level = 0

        while q:
            level_cnt = len(q)

            for _ in range(level_cnt):
                sibling_sum = 0
                cur_node = q.popleft()
                if cur_node.left:
                    sibling_sum += cur_node.left.val
                if cur_node.right:
                    sibling_sum += cur_node.right.val
                
                if cur_node.left:
                    cur_node.left.val = level_sum_list[cur_level] - sibling_sum
                    q.append(cur_node.left)
                
                if cur_node.right:
                    cur_node.right.val = level_sum_list[cur_level] - sibling_sum
                    q.append(cur_node.right)
            cur_level += 1
        root.val = 0
        return root
    

    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        d_sum_map = defaultdict(int)

        def dfs(cur, cur_d):
            if cur == None:
                return
            
            d_sum_map[cur_d] += cur.val
            dfs(cur.left, cur_d + 1)
            dfs(cur.right, cur_d + 1)

            return
        
        def setVal(cur, sibling_sum, cur_d):
            if cur == None:
                return
            
            left_sibling_val = cur.left.val if cur.left else 0
            right_sibling_val = cur.right.val if cur.right else 0

            if cur_d == 0:
                cur.val = 0
            else:
                cur.val = d_sum_map[cur_d] - cur.val - sibling_sum
            setVal(cur.left, right_sibling_val, cur_d+1)
            setVal(cur.right, left_sibling_val, cur_d+1)

        dfs(root, 0)
        setVal(root, 0, 0)
        return root
    

    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        q = deque()
        q.append(root)
        pre_level_sum = root.val

        while q:
            level_cnt = len(q)
            level_sum = 0

            for _ in range(level_cnt):
                cur_node = q.popleft()
                cur_node.val = pre_level_sum - cur_node.val

                sibling_sum = (cur_node.left.val if cur_node.left else 0) + (cur_node.right.val if cur_node.right else 0)

                if cur_node.left:
                    level_sum += cur_node.left.val
                    cur_node.left.val = sibling_sum
                    q.append(cur_node.left)
                
                if cur_node.right:
                    level_sum += cur_node.right.val
                    cur_node.right.val = sibling_sum
                    q.append(cur_node.right)

            pre_level_sum = level_sum
        
        return root
    


                



                
                
        
    
            



