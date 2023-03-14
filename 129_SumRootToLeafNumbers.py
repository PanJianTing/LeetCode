class TreeNode:
    def __init__(self, val= 0, left= None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def rootSum(self, root: TreeNode, sum: int) -> int:

        if root == None:
            return sum
        sum = sum*10 + root.val
        if root.left == None and root.right == None:
            return sum
        if root.left == None:
            return self.rootSum(root.right, sum)
        if root.right == None:
            return self.rootSum(root.left, sum)
        return self.rootSum(root.left, sum) + self.rootSum(root.right, sum)
    
    def dfs(self, root: TreeNode, curr: int) -> int:
        if root == None:
            return 0
        curr = curr * 10 + root.val
        if root.left == None and root.right == None:
            return curr
        return self.dfs(root.left, curr) + self.dfs(root.right, curr)


    def sumNumbers(self, root:TreeNode) -> int:

        # return self.rootSum(root, 0)
        return self.dfs(root ,0)
    

#preorder iterative
class Solution:

    def sumNumbers(self, root:TreeNode) -> int:

        stack = []

        stack.append((root, 0))

        sumCount = 0

        while len(stack) > 0:
            node, val = stack.pop()
            if node is not None:
                val = val * 10 + node.val
                if node.right == None and node.left == None:
                    sumCount += val
                else:
                    stack.append((node.left, val))
                    stack.append((node.right, val))

        return sumCount


# preorder recursion
class Solution:
    sumCount = 0
    def preorder(self, root: TreeNode, count: int):

        if root:
            count = count * 10 + root.val
        
            if root.left == None and root.right == None:
                self.sumCount += count
        
            self.preorder(root.left, count)
            self.preorder(root.right, count)

    def sumNumbers(self, root: TreeNode) -> int:

        self.sumCount = 0
        self.preorder(root, 0)
        return self.sumCount

# Morris
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        rootToLeaf = 0
        curr = 0
        step = 0
        predecessor = None

        while root:

            if root.left:
                predecessor = root.left
                step = 1
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                    step += 1

                if predecessor.right == None:
                    curr = curr * 10 + root.val
                    predecessor.right = root
                    root = root.left
                else:

                    if predecessor.left == None:
                        rootToLeaf += curr
                    
                    for _ in range(0, step):
                        curr //= 10
                    predecessor.right = None
                    root = root.right
            else:
                curr = curr * 10 + root.val

                if root.right == None:
                    rootToLeaf += curr
                root = root.right

        return rootToLeaf
    
            
        
