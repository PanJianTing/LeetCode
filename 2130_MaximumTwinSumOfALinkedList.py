class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next
    
class Solution:
    def pairSum(self, head: ListNode) -> int:
        n = 0
        nMap = {}
        while head:
            nMap[n] = head.val
            head = head.next
            n += 1
            

        half = n >> 1
        ans = 0

        for i in range(0, half):
            lastIdx = n-1-i
            s = nMap[i] + nMap[lastIdx]
            ans = max(ans, s)

        return ans
    
    def pairSum(self, head: ListNode) -> int:
        cur = head
        st = []

        while cur:
            st.append(cur.val)
            cur = cur.next
        cur = head
        halfSize = len(st) >> 1
        ans = 0

        for i in range(0, halfSize):
            ans = max(ans, cur.val + st.pop())
            cur = cur.next
            
        return ans
    
    def pairSum(self, head: ListNode) -> int:
        slow = head
        fast = head

        # find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse
        pre = None
        nextNode = None
        while slow:
            nextNode = slow.next
            slow.next = pre
            pre = slow
            slow = nextNode

        # sum
        st = head
        ans = 0
        while pre:
            ans = max(ans, st.val + pre.val)
            pre = pre.next
            st = st.next

        return ans
    

    def pairSum(self, head: ListNode) -> int:

        slow = head
        fast = head

        pre = None

        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        
        ans = 0

        while slow:
            ans = max(ans, pre.val + slow.val)
            pre = pre.next
            slow = slow.next
        return ans













        
