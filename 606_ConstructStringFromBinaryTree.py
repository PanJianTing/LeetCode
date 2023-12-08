class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if root == None:
            return ""
        
        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)

        if right_str != "":
            return str(root.val) + "("+ left_str + ")" + "("+ right_str +")"
        else:
            if left_str != "":
                return str(root.val) + "("+ left_str + ")"
        
        return str(root.val)
    

    def tree2str(self, root: TreeNode) -> str:
        if root == None:
            return ""
        
        ans = str(root.val)

        if root.left or root.right:
            ans += "("+ self.tree2str(root.left) +")"
        if root.right:
            ans += "(" + self.tree2str(root.right) + ")"

        return ans

    def tree2str(self, root: TreeNode) -> str:
        if root == None:
            return ""
        
        ans = "(" + str(root.val)
        cur = root
        stack = [cur]
        visit = set(stack)
        
        while stack:
            cur = stack[-1]
            
            if cur.left and cur.left not in visit:
                ans += "(" + str(cur.left.val)
                stack.append(cur.left)
                visit.add(cur.left)
                continue

            if cur.right and cur.right not in visit:
                if cur.left == None:
                    ans += "()"
                ans += "(" + str(cur.right.val)
                stack.append(cur.right)
                visit.add(cur.right)
                continue
            
            ans += ")"
            stack.pop()

        return ans[1:-1]
    

    def tree2str(self, root) -> str:
        if root == None:
            return ""
        ans = ""
        stack = [root]
        visit = set()

        while stack:
            cur = stack[-1]

            if cur in visit:
                ans += ")"
                stack.pop()
            else:
                ans += "(" + str(cur.val)

                if cur.left == None and cur.right:
                    ans += "()"
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
                visit.add(cur)
        
        return ans[1:-1]


            
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2
node1.right = node3

node2.left = node4

print(Solution().tree2str(node1))


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2
node1.right = node3

node2.right = node4

print(Solution().tree2str(node1))