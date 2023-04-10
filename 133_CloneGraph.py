class Node:
    def __init__(self, val = 0, neighbors = None) -> None:
        self.val = val
        self.neighbors = neighbors
        


class Solution:

    def __init__(self) -> None:
        self.visit = {}


    def cloneGraph(self, node: Node) -> Node:

        if node == None:
            return None
        
        if node in self.visit:
            return self.visit[node]
        
        clone_node = Node(val=node.val)

        self.visit[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node

