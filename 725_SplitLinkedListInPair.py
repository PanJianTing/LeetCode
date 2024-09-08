class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        N = 0
        cur = head
        res = [None] * k

        while cur:
            N += 1
            cur = cur.next
        
        cur = head
        divid = N // k
        remain = N % k

        for i in range(k):
            cnt = divid
            if remain > 0:
                cnt += 1
                remain -= 1
            
            dummy = cur
            while cur and cnt > 0:
                cnt -= 1
                if cnt:
                    cur = cur.next
                else:
                    cur.next, cur = None, cur.next
            res[i] = dummy
        return res
    

    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        N = 0
        ans = [None] * k
        cur = head

        while cur:
            N += 1
            cur = cur.next
        
        divid = N // k
        remain = N % k
        cur = head

        for i in range(k):
            cnt = divid
            if remain > 0:
                cnt += 1
                remain -= 1
            
            new_part = ListNode(0)
            tail = new_part

            for _ in range(cnt):
                new_node = ListNode(cur.val)
                tail.next = new_node
                tail = tail.next
                cur = cur.next
            ans[i] = new_part.next
        return ans

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

print(Solution().splitListToParts(node1, 5))

