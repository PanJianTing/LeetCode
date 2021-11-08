class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


# Bottom to Top
class Solution:
	def isBalanceHelper(self, root: Optional[TreeNode]) -> (bool, int):
		if root == None:
			return (True, -1)

		## left is balance
		leftBalance, leftH = self.isBalanceHelper(root.left)

		## left is not balance then return
		if leftBalance == False:
			return (False, 0)

		## right is balance
		rightBalance, rightH = self.isBalanceHelper(root.right)

		## right is not balance then return
		if rightBalance == False:
			return (False, 0)

		## return left and right is blance and tree height
		return (abs(leftH - rightH) <= 1, 1 + max(leftH, rightH))

	def isBalanced(self, root: Optional[TreeNode]) -> bool:

		return self.isBalanceHelper(root)[0]

# Top to bottom
class Solution:

	def treeHeight(self, root: Optional[TreeNode]) -> int:
		if root == None:
			return 1;
		else:
			rightHeight = self.treeHeight(root.right) + 1
			leftHeight = self.treeHeight(root.left) + 1

			return max(rightHeight, leftHeight)


	
	## if root is leaf(None) return True
	## computing right subtree height and left subtree height, if over 1, then no balance
	## if right subtree height and left subtree height is less than 1, then check right and left is balance
	def isBalanced(self, root: Optional[TreeNode]) -> bool:

		if root == None:
			return True

		elif abs(self.treeHeight(root.right) - self.treeHeight(root.left)) > 1:
			return False
		else:

			return self.isBalanced(root.left) and self.isBalanced(root.right)