class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num_list = []
        
        while head:
            num_list.append(head.val)
            head = head.next
        
        l = 0
        r = len(num_list) - 1

        while l < r:
            if num_list[l] != num_list[r]:
                return False

            l += 1
            r -= 1
        return True
    
    def isPalindrome(self, head: ListNode) -> bool:
        N = 0
        h = head
        
        while h:
            N += 1
            h = h.next

        cur = head
        pre = None
        idx = 0
        while idx < (N // 2):
            cur = cur.next
            idx += 1

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        while pre:
            if pre.val != head.val:
                return False
        
            pre = pre.next
            head = head.next
        
        return True
    

    def isPalindrome(self, head: ListNode):
        self.headPointer = head

        def check(cur):
            if cur:
                if check(cur.next) == False:
                    return False
                if self.headPointer.val != cur.val:
                    return False
                self.headPointer = self.headPointer.next
            return True
        return check(head)
    

    def isPalindrome(self, head: ListNode) -> ListNode:

        def getMiddle(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow
        
        def reverse(head):
            cur = head
            pre = None
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre
        
        middle_node = getMiddle(head)
        p1 = head
        p2 = reverse(middle_node)

        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    

n1 = ListNode(1)
n2 = ListNode(2)

n1.next = n2

print(Solution().isPalindrome(n1))