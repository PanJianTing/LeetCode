class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    cur_idx = 0 
    def bstToGst(self, root: TreeNode) -> TreeNode:
        val_list = []

        def dfs(cur):
            if cur == None:
                return
            dfs(cur.left)
            val_list.append(cur.val)
            dfs(cur.right)
            return
        
        def change_val(cur):
            if cur == None:
                return
            change_val(cur.left)
            cur.val = new_list[self.cur_idx]
            self.cur_idx += 1
            change_val(cur.right)
            return
        
        dfs(root)
        cur_sum = sum(val_list)
        new_list = []
        cur_val = 0
        
        for i in range(len(val_list)):
            new_list.append(cur_sum - cur_val)
            cur_val += val_list[i]
        
        self.cur_idx = 0
        change_val(root)
        return root
    

    def bstToGst(self, root: TreeNode) -> TreeNode:
        val_list = []

        def inorder(cur):
            if cur == None:
                return
            inorder(cur.left)
            val_list.append(cur.val)
            inorder(cur.right)
        
        def changeVal(cur):
            if cur == None:
                return
            
            changeVal(cur.left)
            change_val = 0
            for n in val_list:
                if n >= cur.val:
                    change_val += n
            cur.val = change_val
            changeVal(cur.right)
            return

        inorder(root)
        changeVal(root)
        return root
    

    def bstToGst(self, root: TreeNode) -> TreeNode:
        all_sum = [0]
        def helper(cur, cur_sum):
            if cur == None:
                return
            
            helper(cur.right, cur_sum)
            cur_sum[0] += cur.val
            cur.val = cur_sum[0]
            helper(cur.left, cur_sum)
            return
        
        helper(root, all_sum)
        return root
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur_sum = 0
        st = []
        cur_node = root

        while st or cur_node:
            while cur_node:
                st.append(cur_node)
                cur_node = cur_node.right
            
            cur_node = st.pop()
            cur_sum += cur_node.val
            cur_node.val = cur_sum
            cur_node = cur_node.left
        
        return root


    

