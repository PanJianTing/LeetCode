class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def gameResult(self, head: ListNode) -> str:
        wins = [0, 0]
        compare = False
        pre = 0

        while head:
            if compare:
                if head.val > pre:
                    wins[1] += 1
                else:
                    wins[0] += 1
            else:
                pre = head.val
            compare = not compare
            head = head.next
        if wins[0] > wins[1]:
            return "Even"
        if wins[1] > wins[0]:
            return "Odd"
        return "Tie"
    
    def gameResult(self, head: ListNode) -> str:
        even_p = 0
        odd_p = 0
        even = head

        while even:
            odd = even.next
            if even.val > odd.val:
                even_p += 1
            else: 
                odd_p += 1
            even = odd.next
        return "Even" if even_p > odd_p else "Odd" if even_p < odd_p else "Tie"
    
    def gameResult(self, head: ListNode) -> str:
        point = 0
        cur = head

        while cur:
            point += 1 if (cur.val > cur.next.val) else -1
            cur = cur.next.next
        return 'Even' if point > 0 else 'Odd' if point < 0 else 'Tie'
