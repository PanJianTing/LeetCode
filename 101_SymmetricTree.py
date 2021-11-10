class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	# symmetric -> left.left == right.right and left.right == right.left
	def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:

		if left == None and right == None:
			return True
		if left == None or right == None:
			return False
		return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)


	def isSymmetric(self, root: Optional[TreeNode]) -> bool:

		return self.isMirror(root.left, root.right)