class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        node_list = []
        cur = head.next
        cur_val = 0

        while cur:
            if cur.val == 0:
                node_list.append(cur_val)
                cur_val = 0
            cur_val += cur.val
            cur = cur.next
        
        dummy = ListNode(0)
        res = dummy

        for n in node_list:
            cur = ListNode(n)
            dummy.next = cur
            dummy = cur
        
        return res.next
    
    def mergeNodes(self, head: ListNode) -> ListNode:
        
        pre_zero = head
        cur = head.next
        cur_val = 0

        while cur:
            if cur.val == 0:
                cur.val = cur_val
                pre_zero.next = cur
                pre_zero = cur
                cur_val = 0
            else:
                cur_val += cur.val
            cur = cur.next
        
        return head.next
    
    def mergeNodes(self, head: ListNode) -> ListNode:
        modify = head.next
        nextSum = modify

        while nextSum:
            cur_sum = 0
            while nextSum.val != 0:
                cur_sum += nextSum.val
                nextSum = nextSum.next
            
            modify.val = cur_sum
            nextSum = nextSum.next
            modify.next = nextSum
            modify = modify.next

        return head.next
    

    def mergeNodes(self, head: ListNode) -> ListNode:
        head = head.next
        if head == None:
            return head
        temp = head
        cur_val = 0
        while temp.val != 0:
            cur_val += temp.val
            temp = temp.next
        head.val = cur_val
        head.next = self.mergeNodes(temp)
        return head
            
    




node0_1 = ListNode(0)
node3 = ListNode(3)
node1 = ListNode(1)
node0_2 = ListNode(0)
node4 = ListNode(4)
node5 = ListNode(5)
node2 = ListNode(2)
node0_3 = ListNode(0)

node0_1.next = node3
node3.next = node1
node1.next = node0_2
node0_2.next = node4
node4.next = node5
node5.next = node2
node2.next = node0_3

print(Solution().mergeNodes(node0_1))