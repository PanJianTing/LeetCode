from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        ans = 0

        while q:
            N = len(q)
            num_list = []
            for i in range(N):
                cur_node = q.popleft()
                num_list.append(cur_node.val)
                
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            
            target = sorted(num_list)
            pos_map = defaultdict(int)
            for i, n in enumerate(num_list):
                pos_map[n] = i
            
            for i in range(N):
                cur_num = num_list[i]
                target_num = target[i]
                if cur_num != target_num:
                    ans += 1

                    cur_pos = pos_map[cur_num]
                    target_pos = pos_map[target_num]
                    
                    num_list[cur_pos], num_list[target_pos] = num_list[target_pos], num_list[cur_pos]
                    pos_map[cur_num] = target_pos
                    pos_map[target_num] = cur_pos


        return ans
    

node1 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)


node1.left = node4
node1.right = node3

node4.left = node7
node4.right = node6

node3.left = node8
node3.right = node5

node8.left = node9
node5.left = node10

print(Solution().minimumOperations(node1))

