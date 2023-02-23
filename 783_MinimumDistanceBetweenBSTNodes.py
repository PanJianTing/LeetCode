import math

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inorderTravel(self, root: TreeNode, nums: list[int]):
        if root == None:
            return
        self.inorderTravel(root.left, nums)
        nums.append(root.val)
        self.inorderTravel(root.right, nums)

    def minDiffInBST(self, root: TreeNode) -> int:
        nums = list()
        self.inorderTravel(root, nums)
        # print(nums)

        ans = math.inf
        for i in range(0, len(nums) - 1):
            diff = nums[i+1] - nums[i]
            if diff < ans:
                ans = diff

        return ans
    
class Solution:
    pre = None
    minValue = math.inf

    def inorderTravel(self, root: TreeNode):
        if root == None:
            return
        self.inorderTravel(root.left)
        if self.pre != None:
            self.minValue = min(self.minValue, root.val - self.pre)
        self.pre = root.val
        self.inorderTravel(root.right)

    def minDiffInBST(self, root: TreeNode) -> int:

        self.inorderTravel(root)
        return self.minValue
    
class Solution:
    pre = -math.inf
    minValue = math.inf

    def minDiffInBST(self, root: TreeNode) -> int:

        if root.left:
            self.minDiffInBST(root.left)
        self.minValue = min(self.minValue, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.minValue


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def helper(root,low,high):
            if root == None:
                return high-low
            
            left = helper(root.left,low,root.val)
            right = helper(root.right,root.val,high)
            return min(left,right)
        return helper(root,float("-inf"),float("inf"))
    
