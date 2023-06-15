class TreeNode:
    def __init__(self, val= 0, left= None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nums = []
        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)
        # print(nums)
        N = len(nums)
        minnum = 100000000
        for i in range(1, N):
            minnum = min(minnum, nums[i]- nums[i-1])
        
        return minnum
    
    def getMinimumDifference(self, root) -> int:
        global minnum, pre
        minnum = 100000000
        pre = -10000000000
        
        def inorder(node):
            global minnum, pre
            if node == None:
                return
            inorder(node.left)
            minnum, pre = min(minnum, node.val - pre), node.val
            inorder(node.right)
        inorder(root)
        return minnum

    
