class TreeNode:
	def __init__(self, val= 0, left= None, right= None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:

		if root == None:
			return 0
		elif root.right == None and root.left == None:
			return 1
		else:
			rightDepth = 0
			leftDepth = 0

			rightDepth += self.maxDepth(root.right)
			leftDepth += self.maxDepth(root.left)

			return max(rightDepth, leftDepth) + 1


	def maxDepth(self, root: Optional[TreeNode]) -> int:

		if root == None:
			return 0
		elif root.right == None and root.left == None:
			return 1
		else:
			return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1