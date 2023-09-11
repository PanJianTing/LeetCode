class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head, cnt):
        pre = None
        ptr = head

        for _ in range(cnt):
            temp = ptr
            ptr = ptr.next
            temp.next = pre
            pre = temp
        head.next = ptr
        return pre
    
    def reverseBetween(self, head, left, right):

        if left == right:
            return head

        now = 1
        ptr = head
        pre = None
        while ptr:
            if now == left:
                # revers start
                cnt = right - left + 1
                if pre:
                    pre.next = self.reverse(ptr, cnt)
                else:
                    head = self.reverse(ptr, cnt)
            
            pre = ptr
            ptr = ptr.next
            now += 1
        return head
    
    def reverseBetween(self, head, m, n):
        right = head
        left = head
        change = True
        

        def recurse(curRight, curM, curN):
            nonlocal left, change
            if curN == 1:
                return
            
            curRight = curRight.next

            if curM > 1:
                left = left.next
            
            recurse(curRight, curM-1, curN-1)

            if left == curRight or curRight.next == left:
                change = False
            
            if change:
                left.val, curRight.val = curRight.val, left.val
                left = left.next
        
        recurse(right, m, n)
        return head
    
    def reverseBetween(self, head, left, right):
        cur = head
        pre = None
        N = 1

        while cur:
            if N == left:
                tail = cur
                con = pre
                cnt = right - left + 1
                for _ in range(cnt):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                if con:
                    con.next = pre
                else:
                    head = pre
                tail.next = cur
            N += 1
            pre = cur
            if cur:
                cur = cur.next
        return head
    
    def reverseBetween(self, head, m, n):
        if head == None:
            return head
        cur = head
        pre = None
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1
        
        con = pre
        tail = cur
        while n > 0:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            n -= 1
        
        if con != None:
            con.next = pre
        else:
            head = pre
        
        tail.next = cur
        return head


            
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
# node1 = ListNode()

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

h = Solution().reverseBetween(node1, 2, 4)

while h:
    print(h.val)
    h = h.next
print("=======")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
h = Solution().reverseBetween(node1, 1, 4)

while h:
    print(h.val)
    h = h.next

print("=========")
h = Solution().reverseBetween(node6, 1, 1)

while h:
    print(h.val)
    h = h.next