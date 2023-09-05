class Node:
    def __init__(self, x, next = None, random = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):

        randomIdx = {}
        temp = head
        N = 0
        while temp:
            randomIdx[temp] = N
            N += 1
            temp = temp.next

        newHead = Node(-1)
        old_point = head
        new_point = newHead
        randomList = [None] * N
        new_random_map = {}
        idx = 0


        while old_point:
            new_point.next = Node(old_point.val)
            if old_point.random:
                randomList[idx] = randomIdx[old_point.random]
            new_point = new_point.next
            old_point = old_point.next
            new_random_map[idx] = new_point
            idx += 1

        for i, idx in enumerate(randomList):
            if idx != None:
                new_random_map[i].random = new_random_map[idx]
                
        return newHead.next
    

    def __init__(self) -> None:
        self.visitedNode= {}

    def copyRandomList(self, head):
        if head == None:
            return None
        
        if head in self.visitedNode:
            return self.visitedNode[head]

        node = Node(head.val)
        self.visitedNode[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
    
    def copyRandomList(self, head):
        if head == None:
            return None
        
        tempHead = head
        visitedNode = {}

        while head:    
            
            if head in visitedNode:
                copyNode = visitedNode[head]
            else:
                copyNode = Node(head.val)
                visitedNode[head] = copyNode

            if head.next in visitedNode:
                copyNode.next = visitedNode[head.next]
            else:
                if head.next:
                    next_copy_node = Node(head.next.val)
                    copyNode.next = next_copy_node
                    visitedNode[head.next] = next_copy_node

            if head.random in visitedNode:
                copyNode.random = visitedNode[head.random]
            else:
                if head.random:
                    random_copy_node = Node(head.random.val)
                    copyNode.random = random_copy_node
                    visitedNode[head.random] = random_copy_node
            
            head = head.next

        return visitedNode[tempHead]
    
    def cloneNode(self, node):
        if node:
            if node in self.visitedNode:
                return self.visitedNode[node]
            else:
                self.visitedNode[node] = Node(node.val)
                return self.visitedNode[node]
        return None
    
    def copyRandomList(self, head):

        if not head:
            return Node
        
        oldNode = head
        newNode = Node(head.val)
        self.visitedNode[head] = newNode

        while oldNode:

            newNode.next = self.cloneNode(oldNode.next)
            newNode.random = self.cloneNode(oldNode.random)

            oldNode = oldNode.next
            newNode = newNode.next
        
        return self.visitedNode[head]
    

    def copyRandomList(self, head):
        if not head:
            return None
        
        temp = head

        while temp:
            copy_node = Node(temp.val)
            copy_node.next = temp.next
            temp.next = copy_node
            temp = copy_node.next

        temp = head
        while temp:
            if temp.next and temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        temp = head
        new_head = head.next

        while temp:
            next_ptr = temp.next.next
            if temp.next:
                next_ptr = temp.next.next
                if temp.next.next:
                    temp.next.next = temp.next.next.next
            temp = next_ptr
        return new_head

    def copyRandomList(self, head):
        if not head:
            return None
        
        temp = head

        while temp:
            copy_node = Node(temp.val)
            copy_node.next = temp.next
            temp.next = copy_node
            temp = copy_node.next

        temp = head
        while temp:
            if temp.next and temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        
        old_ptr = head
        new_ptr = head.next
        new_head = head.next

        while old_ptr:
            old_ptr.next = old_ptr.next.next
            if new_ptr.next:
                new_ptr.next = new_ptr.next.next

            old_ptr = old_ptr.next
            new_ptr = new_ptr.next
        return new_head

node0 = Node(7)
node1 = Node(13)
node2 = Node(11)
node3 = Node(10)
node4 = Node(1)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4


node0.random = None
node1.random = node0
node2.random = node4
node3.random = node2
node4.random = node0


head = Solution().copyRandomList(node0)

while head:
    if head.random:
        print(head.val, head.random, head.random.val)
    else:
        print(head.val, head.random)
    head = head.next