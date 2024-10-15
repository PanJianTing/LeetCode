class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestPerfectSubtree(self, root: TreeNode, k: int) -> int:

        num_tree = []

        def dfs(cur):
            if cur == None:
                return 0, 0, True
            
            cur_perfect = True
            left_level, left_count, left_perfect = dfs(cur.left)
            right_level, right_count, right_perfect = dfs(cur.right)

            if left_level == right_level and left_perfect and right_perfect:
                num_tree.append(1 + left_count + right_count)
            else:
                cur_perfect = False
            
            return 1 + max(left_level, right_level), 1 + left_count + right_count, cur_perfect

        dfs(root)

        if len(num_tree) < k:
            return -1
        return sorted(num_tree, reverse=True)[k-1]
    

    def kthLargestPerfectSubtree(self, root: TreeNode, k: int) -> int:

        num_tree = []

        def dfs(cur):
            if cur == None:
                return 0
            
            l = dfs(cur.left)
            r = dfs(cur.right)

            if l == r and l >= 0:
                num_tree.append(1 + l + r)
                return 1 + l + r
            
            return -1

        dfs(root)

        if len(num_tree) < k:
            return -1
        return sorted(num_tree, reverse=True)[k-1]