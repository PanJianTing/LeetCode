class ListNode:
    def __init__(self, val= 0, next= None) -> None:
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        n = 0
        temp = head
        while temp:
            temp = temp.next
            n += 1

        sInx = k-1
        eInx = n-k

        start = head
        end = head

        for i in range(0, n):
            if i < sInx:
                start = start.next
            if i < eInx:
                end = end.next
        
        start.val, end.val = end.val, start.val
        
        return head
    
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        s, e, temp = None, None, head
        
        while temp:
            k -= 1

            if e:
                e = e.next
            if k == 0:
                s = temp
                e = head
            temp = temp.next
        
        s.val, e.val = e.val, s.val

        return head

            