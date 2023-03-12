from queue import PriorityQueue

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
# my
class Solution:

    def mergeList(self, node1: ListNode, node2: ListNode) -> ListNode:

        root = ListNode(None)
        node = root

        while node1 and node2:

            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next

        if node1:
            node.next = node1
        elif node2:
            node.next = node2

        return root.next



    def mergeKLists(self, lists: list[ListNode]) -> ListNode:

        k = len(lists)

        if k > 2:
            mid = k // 2
            node1 = self.mergeKLists(lists[0:mid])
            node2 = self.mergeKLists(lists[mid:])
            return self.mergeList(node1, node2)
        elif k == 2:

            return self.mergeList(lists[0], lists[1])
        elif k == 1:
            return lists[0]
        
        return None

# brute Force, Time: O(NlogN), Space = O(2n) = O(n)  
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        nodes.sort()
        for x in nodes:
            point.next = ListNode(x)
            point = point.next
        return head.next


#PriorityQ, time: O(Nlogk), space: O(n)
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:

        h = p = ListNode(0)
        q = PriorityQueue()

        for l in lists:
            if l:
                q.put((l.val, l))
        
        while q.empty() == False:
            val, node = q.get()
            p.next = ListNode(val)
            p = p.next
            node = node.next
            if node:
                q.put((node.val. node))

        return h.next


# divid and conquer, time: O(Nlogk), space: O(1)
class Solution:

    def mergeList(self, node1: ListNode, node2: ListNode) -> ListNode:

        root = ListNode(None)
        node = root

        while node1 and node2:

            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next

        if node1:
            node.next = node1
        elif node2:
            node.next = node2

        return root.next

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:

        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.mergeList(lists[i], lists[i + interval])

            interval *= 2

        return lists[0] if k > 0 else None