class ListNode:
    def __init__(self, val= 0, next= None) -> None:
        self.val = 0
        self.next = next

class Solution:
    def swap(self, head: ListNode):
        if head and head.next:
            head.val, head.next.val = head.next.val, head.val
            self.swap(head.next.next.next)
        return
    


    def swapPairs(self, head: ListNode) -> ListNode:
        self.swap(head)
        return head
    


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        b = head.next

        head.next = self.swapPairs(b.next)
        b.next = head
        return b
    

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        preNode = dummy
        while head and head.next:
            a = head
            b = head.next

            # swap
            preNode.next = b
            a.next = b.next
            b.next = a

            preNode = a
            head = a.next

        return dummy.next
        