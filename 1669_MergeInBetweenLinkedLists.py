class ListNode:
    def __init__(self, val= 0, next= None) -> None:
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, h1: ListNode, a: int, b: int, h2: ListNode) -> ListNode:
        n1 = h1
        n2 = h1
        cur_1 = 0
        cur_2 = 0

        while n1 and cur_1 < a-1:
            n1 = n1.next
            cur_1 += 1

        while n2 and cur_2 < b+1:
            n2 = n2.next
            cur_2 += 1
        
        n1.next = h2
        
        while h2 and h2.next:
            h2 = h2.next
        
        h2.next = n2
        return h1

    def mergeInBetween(self, h1: ListNode, a: int, b: int, h2: ListNode) -> ListNode:
        mergeArray = []
        cur = h1
        cur_idx = 0

        while cur and cur_idx < a:
            mergeArray.append(cur.val)
            cur = cur.next
            cur_idx += 1
            
        while h2:
            mergeArray.append(h2.val)
            h2 = h2.next
    
        while cur:
            if cur_idx > b:
                mergeArray.append(cur.val)
            cur_idx += 1
            cur = cur.next
        
        dummy = ListNode(-1)
        cur = dummy
        for num in mergeArray:
            newNode = ListNode(num)
            cur.next = newNode
            cur = cur.next
            
        return dummy.next
    
    def mergeInBetween(self, h1: ListNode, a: int, b: int, h2: ListNode) -> ListNode:
        st = h1
        end = h1
        cur_idx = 0

        while end and cur_idx < b+1:
            if cur_idx == a-1:
                st = end
            end = end.next
            cur_idx += 1
        st.next = h2

        while h2 and h2.next:
            h2 = h2.next
        
        h2.next = end

        return h1