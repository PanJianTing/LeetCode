class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight) -> None:
        self.val = val
        self.isLeaf         = isLeaf
        self.topLeft        = topLeft
        self.topRight       = topRight
        self.bottomLeft     = bottomLeft
        self.bottomRight    = bottomRight

class Solution:
    def isLeaf(self, grid: list[list[int]]) -> bool:
        return all(grid[i][j] == grid[0][0] 
                   for i in range(len(grid)) for j in range(len(grid[i])))

    def construct(self, grid: list[list[int]]) -> 'Node':
        if not grid: 
            return None
        
        if self.isLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)
        n = len(grid)
        return Node("*", 
                    False, 
                    self.construct([row[:n/2] for row in grid[:n/2]]),
                    self.construct([row[n/2:] for row in grid[:n/2]]),
                    self.construct([row[:n/2] for row in grid[n/2:]]),
                    self.construct([row[n/2:] for row in grid[n/2:]]))
    
    def construct(self, grid: list[list[int]]) -> 'Node':

        root = Node(True, True, None, None, None, None)
        if len(set([item for row in grid for item in row])) == 1:
            root.val = bool(grid[0][0])
        else:
            root.isLeaf = False
            size = len(grid)
            root.topLeft        = self.construct([row[:size // 2] for row in grid[:size//2]])
            root.topRight       = self.construct([row[size // 2:] for row in grid[:size//2]])
            root.bottomLeft     = self.construct([row[:size // 2] for row in grid[size//2:]])
            root.bottomRight    = self.construct([row[size // 2:] for row in grid[size//2:]])
        return root

