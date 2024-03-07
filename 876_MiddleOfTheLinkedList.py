class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    

    def middleNode(self, head: ListNode) -> ListNode:
        node_list = []

        while head:
            node_list.append(head)
            head = head.next
        
        return node_list[len(node_list)//2]