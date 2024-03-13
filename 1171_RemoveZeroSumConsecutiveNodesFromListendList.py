from collections import defaultdict

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        st = dummy
        
        while st:
            prefixSum = 0
            end = st.next
            while end:
                prefixSum += end.val
                if prefixSum == 0:
                    st.next = end.next
                    break
                end = end.next
            st = st.next
        return dummy.next
    
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        cur = dummy
        prefixSum_map = defaultdict(ListNode)
        prefixSum = 0
        while cur:
            prefixSum += cur.val
            prefixSum_map[prefixSum] = cur
            cur = cur.next
        
        cur = dummy
        prefixSum = 0

        while cur:
            prefixSum += cur.val
            cur.next = prefixSum_map[prefixSum].next
            cur = cur.next
        
        return dummy.next
    
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        cur = dummy
        prefixSum_map = defaultdict(ListNode)
        prefixSum = 0

        while cur:
            prefixSum += cur.val

            if prefixSum in prefixSum_map:
                pre = prefixSum_map[prefixSum]
                cur = pre.next

                p = pre + cur.val
                while p != prefixSum:
                    del prefixSum_map[p]
                    cur = cur.next
                    p += cur.val

                pre.next = cur.next
            else:
                prefixSum_map[prefixSum] = cur
            cur = cur.next
        
        return dummy.next
    