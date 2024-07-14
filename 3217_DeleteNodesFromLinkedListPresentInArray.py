class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        cur = head
        nums = set(nums)

        while cur:
            if cur.val not in nums:
                pre.next = cur
                pre = cur
            cur = cur.next
        pre.next = None
        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

res = Solution().modifiedList([1,2,3],node1)

while res:
    print(res.val)
    res = res.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(2)
node5 = ListNode(1)
node6 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

res = Solution().modifiedList([1],node1)

while res:
    print(res.val)
    res = res.next