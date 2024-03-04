class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, i: int) -> ListNode:
        N = 0
        cur = head
        pre = None
        while cur:
            N += 1
            cur = cur.next
        target = N - i + 1
        idx = 1
        cur = head
        if target == 1:
            return head.next
        while cur:
            if idx == target:
                pre.next = cur.next
                break
            pre = cur
            cur = cur.next
            idx += 1
        return head
    
    def removeNthFromEnd(self, head: ListNode, i: int) -> ListNode:
        N = 0
        dummy = ListNode(-1, head)
        cur = head
        while cur:
            N += 1
            cur = cur.next
        target = N - i
        pre = dummy
        while target > 0:
            pre = pre.next
            target -= 1
        pre.next = pre.next.next
        return dummy.next
    

    def removeNthFromEnd(self, head: ListNode, i: int) -> ListNode:
        dummy = ListNode(-1, head)
        pre1 = dummy
        pre2 = dummy
        for _ in range(i):
            pre1 = pre1.next
        
        while pre1:
            pre1 = pre1.next
            pre2 = pre2.next
        pre2.next = pre2.next.next
        return dummy.next
        
