class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    indexMap = {}
    postorder = []
    inorder = []
    post_idx = 0

    def helper(self, left: int, right: int) -> TreeNode:

        if left > right:
            return None
        
        rootVal = self.postorder[self.post_idx]
        root = TreeNode(rootVal)

        index = self.indexMap[rootVal]

        self.post_idx -= 1
        root.right = self.helper(index+1, right)
        root.left = self.helper(left, index-1)
        return root



    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:

        self.postorder = postorder
        self.inorder = inorder

        self.post_idx = len(postorder) - 1

        idx = 0
        for val in inorder:
            self.indexMap[val] = idx
            idx += 1

        return self.helper(0, self.post_idx)
    
# my
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:

        if len(inorder) == 0:
            return None
        
        val = postorder.pop()
        root = TreeNode(val)
        index =  inorder.index(val)
        root.right = self.buildTree(inorder[index + 1:], postorder)
        root.left = self.buildTree(inorder[0:index], postorder)

        return root

# solution
class Solution:
    postorder = []
    indexMap = {}
    def helper(self, left: int, right: int) -> TreeNode:

        if left > right:
            return None
        
        val = self.postorder.pop()
        root = TreeNode(val)
        index = self.indexMap[val]
        root.right = self.helper(index + 1, right)
        root.left = self.helper(left, index - 1)

        return root


    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:

        self.indexMap = {}
        self.postorder = postorder
        for idx, val in enumerate(inorder):
            self.indexMap[val] = idx
        return self.helper(0, len(postorder) - 1)
