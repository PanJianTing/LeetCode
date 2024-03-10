from collections import defaultdict

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = ValueError
        self.next = next

class Solution:
    def frequenciesOfElements(self, head: ListNode) -> ListNode:
        freq_map = defaultdict(int)

        while head:
            freq_map[head.val] += 1
            head = head.next

        dummy = ListNode(-1)
        cur = dummy

        for n in freq_map.values():
            freq_node = ListNode(n)
            cur.next = freq_node
            cur = freq_node
        return dummy.next
    
    def frequenciesOfElements(self, head: ListNode) -> ListNode:
        node_map = defaultdict(ListNode)

        dummy = ListNode(-1)
        cur = dummy

        while head:
            if head.val in node_map:
                node_map[head.val].val += 1
            else:
                next_node = ListNode(1)
                cur.next = next_node
                cur = next_node
                node_map[head.val] = next_node
            
            head = head.next

        return dummy.next
    
    