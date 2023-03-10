class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

class Solution:

    # time complexity: O(n), Space complexity: O(n), using array
    def detectCycle(self, head: ListNode) -> ListNode:

        nodeList = []

        while head != None:
            if head in nodeList:
                return head
            nodeList.append(head)
            head = head.next

        return None
    
    # time complexity: O(n), Space complexity: O(n), using array
    def detectCycle(self, head: ListNode) -> ListNode:
        nodeList = set()

        while head != None:
            if head in nodeList:
                return head
            nodeList.add(head)
            head = head.next
        
        return None
    

    def getInterSection(self, head: ListNode) -> ListNode:

        p1 = p2 = head

        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return p1

        return None
    
    def detectCycle(self, head: ListNode) -> ListNode:

        intersection = self.getInterSection(head)

        if intersection != None:
            p1 = head
            p2 = intersection

            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            
            return p1
        
        return None
