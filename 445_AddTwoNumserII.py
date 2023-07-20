class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:

    def reverse(self, head) -> ListNode:
        
        pre = None

        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next 
        return pre


    def addTwoNumbers(self, l1, l2) -> ListNode:
        
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        carry = 0
        head = None

        while l1 or l2 or carry:
            l1Val = 0
            l2Val = 0
            
            if l1:
                l1Val = l1.val
                l1 = l1.next
            
            if l2:
                l2Val = l2.val
                l2 = l2.next

            digitSum = l1Val + l2Val + carry
            if digitSum > 9:
                carry = digitSum // 10
                digitSum = digitSum % 10
            else:
                carry = 0

            
            temp = ListNode(digitSum)
            temp.next = head
            head = temp
        return head
    
    def addTwoNumbers(self, l1, l2) -> ListNode:
        l1S = []
        l2S = []

        while l1:
            l1S.append(l1.val)
            l1 = l1.next
        
        while l2:
            l2S.append(l2.val)
            l2 = l2.next

        ans = ListNode()
        carry = 0
        totalSum = 0

        while l1S or l2S:
            if l1S:
                totalSum += l1S.pop()
            
            if l2S:
                totalSum += l2S.pop()

            ans.val = totalSum % 10
            carry = totalSum // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            totalSum = carry

        return ans if carry else ans.next
    

    def reverseList(self, head) -> ListNode:
        pre = None

        while head:
            n = head.next
            head.next = pre
            pre = head
            head = n
        return pre
    
    def addTwoNumbers(self, l1, l2) -> ListNode:
        r1 = self.reverseList(l1)
        r2 = self.reverseList(l2)

        totalSum = 0
        carry = 0
        ans = ListNode()
    
        while r1 or r2:
            if r1:
                totalSum += r1.val
                r1 = r1.next
            if r2:
                totalSum += r2.val
                r2 = r2.next
            
            ans.val = totalSum % 10
            carry = totalSum // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            totalSum = carry

        return ans if carry else ans.next

    
l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
l2 = ListNode(5, ListNode(6, ListNode(4)))

h = Solution().addTwoNumbers(l1, l2)
print("f")
while h:
    print(h.val)
    h = h.next


