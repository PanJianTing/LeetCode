class ListNode:
	def __init__(self, val=0, next=None):
		self.val  = val
		self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    	length = self.getLength(head)
    	if length == 0 or length == 1:
    		return head
    	
    	k %= length
    	tail = head

    	while tail.next:
    		tail = tail.next

    	tail.next = head
    	root = ListNode(0, head)

    	for _ in range(0, length - k - 1):
    		head = head.next
    	root.next = head.next
    	head.next = None

    	return root.next

    def getLength(self, head: ListNode) -> int:

    	count = 0
    	while head:
    		count += 1
    		head = head.next

    	return count


class Solution:
	def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		
		if head == None or head.next == None:
			return head

		now = head
		count = 0
		while now:
			count += 1
			now = now.next

		k %= count

		for i in range(0, k):
			tail = None
			second = None
			now = head
			while now:
				tail = now
				if now.next:
					if now.next.next == None:
						second = now

				now = now.next

			tail.next = head
			second.next = None

			head = tail

		return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5



ans = Solution().rotateRight(node1, 2)

print("#########")
while ans:
	print(ans.val)
	ans = ans.next



