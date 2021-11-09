class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	# iterator
	def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

		nums = []

		if root == None:
			return nums

		stack = [root]

		while stack:
			node = stack.pop()
			if node:
				nums.append(node.val)
				if node.right:
					stack.append(node.right)
				if node.left:
					stack.append(node.left)
		return nums


	# recurssion
	def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

		nums = []

		if root == None:
			return nums
		else:
			nums.append(root.val)
			nums.extend(self.preorderTraversal(root.left))
			nums.extend(self.preorderTraversal(root.right))


		return nums




