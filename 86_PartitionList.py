class ListNode:
    def __init__(self, val= 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x) -> ListNode:
        greater = []
        less = []

        cur = head
        while cur:
            if cur.val < x:
                less.append(cur.val)
            else:
                greater.append(cur.val)
            cur = cur.next

        next = None

        for idx in range(len(greater) -1, -1, -1):
            node = ListNode(greater[idx], next)
            next = node
        
        for idx in range(len(less) - 1, -1, -1):
            node = ListNode(less[idx], next)
            next = node
        
        return next
    
    def partition(self, head, x):

        before = ListNode(0)
        after = ListNode(0)
        bh = before
        ah = after

        while head:
            if head.val < x:
                before.next = head
                before = before.next
                head = head.next
                before.next = None
            else:
                after.next = head
                after = after.next
                head = head.next
                after.next = None

        before.next = ah.next
        return bh.next
    
    def partition(self, head, x):

        before = ListNode(0)
        after = ListNode(0)
        bh = before
        ah = after

        while head:
            if head.val < x:
                before.next = head
                before = before.next
                
            else:
                after.next = head
                after = after.next

            head = head.next

        after.next = None
        before.next = ah.next
        return bh.next



node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = Solution().partition(node1, 3)

while head:
    print(head.val)
    head = head.next


