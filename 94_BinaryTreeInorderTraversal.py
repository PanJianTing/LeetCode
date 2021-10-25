class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = None
		self.right = None


# iteration
class Solution:
	def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

		stack = []
		result = []

		while root is not None or stack != []:
			while root is not None:
				stack.append(root)
				root = root.left
			print(stack)
			root = stack.pop()
			result.append(root.val)
			root = root.right

		return result


# recurrence
class Solution:
	def travelsal(self, root: Optional[TreeNode], nodes: list[int]):

		if root != None:
			self.travelsal(root.left, nodes)
			nodes.append(root.val)
			self.travelsal(root.right, nodes)
	


	def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

		nodes = []

		self.travelsal(root, nodes)

		return nodes

		




