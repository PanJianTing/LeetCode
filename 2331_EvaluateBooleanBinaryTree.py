from collections import defaultdict

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        if root.left == None and root.right == None:
            return root.val == 1
        
        if root.val == 2:
            return self.evaluateTree(root.left) | self.evaluateTree(root.right)
    
        return self.evaluateTree(root.left) & self.evaluateTree(root.right)
    
    def evaluateTree(self, root: TreeNode) -> bool:
        st = [root]
        evaluate_map = defaultdict(bool)

        while st:
            top_node = st[-1]

            if top_node.left == None and top_node.right == None:
                evaluate_map[top_node] = top_node.val == 1
                st.pop()
                continue
            
            if top_node.left in evaluate_map and top_node.right in evaluate_map:
                if top_node.val == 2:
                    evaluate_map[top_node] = evaluate_map[top_node.left] | evaluate_map[top_node.right]
                else:
                    evaluate_map[top_node] = evaluate_map[top_node.left] & evaluate_map[top_node.right]
                st.pop()
            else:
                st.append(top_node.left)
                st.append(top_node.right)
        return evaluate_map[root]
    

node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(0)
node5 = TreeNode(1)


node1.left = node2
node1.right = node3

node3.left = node4
node3.right = node5

print(Solution().evaluateTree(node1))

    
    
