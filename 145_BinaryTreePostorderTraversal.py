class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
		if root == None:
			return []
		stack = []
		result = []

		while root or stack != []:
			while root:
				stack.append(root)
				root = root.left
			temp = stack[-1].right
			if temp:
				root = temp
			else:
				temp = stack.pop()
				result.append(temp.val)
				while stack and temp == stack[-1].right:
					temp = stack.pop()
					result.append(temp.val)

		return result

class Solution:
	def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

		nums = []

		if root == None:
			return []
		else:
			nums.extend(self.postorderTraversal(root.left))
			nums.extend(self.postorderTraversal(root.right))
			nums.append(root.val)
		return nums

