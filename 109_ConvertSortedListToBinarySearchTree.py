class ListNode:
    def __init__(self, val= 0, next= None ):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:

    def bst(self, arr: list[int]) -> TreeNode:

        count = len(arr)

        if count == 0:
            return None
        elif count == 1:
            return TreeNode(arr[0])
        else:
            mid = count >> 1
            leftNode = self.bst(arr[0:mid])
            rightNode = self.bst(arr[mid+1:])

            root = TreeNode(arr[mid])
            root.left = leftNode
            root.right = rightNode
            return root
            

    def sortedListToBST(self, head: ListNode) -> TreeNode:

        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.bst(arr)
    
class Solution:

    def findMiddle(self, head: ListNode) -> ListNode:

        slow = head
        fast = head
        pre = None
        
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        if pre:
            pre.next = None

        return slow


    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if not head:
            return None
        
        mid = self.findMiddle(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
    
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        def toBST(left: int, right: int) -> TreeNode:

            if left > right:
                return None

            mid = left + ((right - left) >> 1)

            node = TreeNode(arr[mid])
            

            if left == right:
                return node
            
            node.left = toBST(left, mid-1)
            node.right = toBST(mid+1, right)
            return node
        return toBST(0, len(arr)-1)
    

class Solution:
    def getSize(self, head: ListNode) -> int:

        ptr = head
        c = 0
        while ptr:
            c += 1
            ptr = ptr.next
        return c

    def sortedListToBST(self, head: ListNode) -> TreeNode:

        size = self.getSize(head)

        def convert(l, r) -> TreeNode:

            nonlocal head

            if l > r:
                return None
            
            mid = l + ((r - l) >> 1)

            left = convert(l, mid - 1)

            node = TreeNode(head.val)
            node.left = left

            head = head.next

            node.right = convert(mid+1, r)
            return node
        
        return convert(0, size - 1)



node1 = ListNode(-10)
node2 = ListNode(-3)
node3 = ListNode(0)
node4 = ListNode(5)
node5 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

Solution().sortedListToBST(node1)

