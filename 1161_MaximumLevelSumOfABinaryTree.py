from collections import deque
from collections import defaultdict

class TreeNode:
    def __init__(self, val= 0, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root) -> int:

        q = deque()
        q.append(root)

        minLevel = 1
        maxSum = root.val
        nowLevel = 1

        while q:
            N = len(q)
            tempSum = 0
            for _ in range(N):
                node = q.popleft()
                tempSum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if tempSum > maxSum:
                maxSum = tempSum
                minLevel = nowLevel
            nowLevel += 1
        return minLevel
    
    def maxLevelSum(self, root) -> int:
        levelSum = defaultdict(int)

        def travers(node, level):
            if node == None:
                return
            
            levelSum[level] += node.val
            travers(node.left, level+1)
            travers(node.right, level+1)
        
        travers(root, 1)

        minLevel = 1
        maxSum = root.val
        for level in levelSum.keys():

            if levelSum[level] > maxSum:
                minLevel = level
                maxSum = levelSum[level]
        return minLevel
    
    def maxLevelSum(self, root) -> int:
        levelSums = []

        def dfs(node, level):
            if node == None:
                return
            
            if len(levelSums) == level:
                levelSums.append(node.val)
            else:
                levelSums[level] += node.val
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)
        return levelSums.index(max(levelSums)) + 1

            