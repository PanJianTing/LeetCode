class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        cur = head
        cur_list = []
        gcd_list = []

        while cur:
            cur_list.append(cur.val)
            cur = cur.next
        
        def findGCD(a, b):
            if b > a:
                return findGCD(b, a)
            if b == 0:
                return a
            return findGCD(b, a % b)
        
        print(findGCD(18, 6))
        
        for i in range(1, len(cur_list)):
            gcd_list.append(findGCD(cur_list[i-1], cur_list[i]))
        
        dummy = ListNode(0)
        cur = dummy

        for i in range(len(cur_list)):
            cur.next = ListNode(cur_list[i])
            cur = cur.next
            if i < len(gcd_list):
                cur.next = ListNode(gcd_list[i])
                cur = cur.next

        return dummy.next
    

    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        cur = head.next
        pre = head

        def findGCD(a, b):
            if b == 0:
                return a
            return findGCD(b, a % b)
        
        while cur:
            new_node = ListNode(findGCD(pre.val, cur.val))
            pre.next = new_node
            new_node.next = cur
            pre = cur
            cur = cur.next
        
        return head

        
            

    


node1 = ListNode(18)
node2 = ListNode(6)
node3 = ListNode(10)
node4 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4


print(Solution().insertGreatestCommonDivisors(node1))
    



