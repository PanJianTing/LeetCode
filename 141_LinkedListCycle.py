class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        listSet = set()

        while head:
            if head in listSet:
                return True
            listSet.add(head)
            head = head.next
        return False
    
    def hasCycle(self, head):
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
    def hasCycle(self, head: ListNode) -> bool:
        num = set()
        cur = head

        while cur:
            if cur in num:
                return True
            num.add(cur)
            cur = cur.next
        return False