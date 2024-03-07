class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1, head)
        pre = dummy
        slow = head
        fast = head

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = slow.next
        return dummy.next
    
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if head.next == None:
            return None
        
        p1 = head
        p2 = head

        count = 0
        while p1:
            count += 1
            p1 = p1.next
        
        target = count//2 - 1
        while target > 0:
            p2 = p2.next
            target -= 1

        p2.next = p2.next.next
        return head
    
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if head.next == None:
            return None
        
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head