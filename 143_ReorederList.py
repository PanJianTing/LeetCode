class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode):
        if head.next == None:
            return 
        pre = None
        slow = head
        fast = head

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        if pre:
            pre.next = None
        
        pre = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        h1 = head
        h2 = pre

        while h1 and h2:
            temp1, temp2 = h1.next, h2.next
            h1.next = h2
            if temp1:
                h2.next = temp1
            h1, h2 = temp1, temp2

    def reorderList(self, head: ListNode):
        if head == None:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow
        pre = None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        
        h1 = head
        h2 = pre
        
        while h2.next:
            h1.next, h1 = h2, h1.next
            h2.next, h2 = h1, h2.next
        
    def reorderList(self, head: ListNode):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        pre = None
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        h1 = head
        h2 = pre
        while h2:
            temp1, temp2 = h1.next, h2.next
            h1.next = h2
            h2.next = temp1
            h1, h2 = temp1, temp2
        
