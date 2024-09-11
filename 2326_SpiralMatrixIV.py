class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, M: int, N: int, head: ListNode) -> list[list[int]]:
        res = [[-1] * N for _ in range(M)]

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir = 0
        cur = head
        cur_m = 0
        cur_n = 0

        while cur:
            res[cur_m][cur_n] = cur.val
            dm, dn = dirs[cur_dir]
            next_m = cur_m + dm
            next_n = cur_n + dn
            if 0 <= next_m < M and 0 <= next_n < N and res[next_m][next_n] == -1:
                cur_m = next_m
                cur_n = next_n
            else:
                cur_dir = (cur_dir + 1) % 4
                dm, dn = dirs[cur_dir]
                cur_m += dm
                cur_n += dn

            cur = cur.next
            
        return res
    
    def spiralMatrix(self, ROW: int, COL: int, head: ListNode) -> list[list[int]]:
        res = [[-1] * COL for _ in range(ROW)]

        top = 0
        down = ROW-1
        left = 0
        right = COL-1

        while head:

            for i in range(left, right+1):
                if head:
                    res[top][i] = head.val
                    head = head.next
            top += 1

            for i in range(top, down+1):
                if head:
                    res[i][right] = head.val
                    head = head.next
            right -= 1

            for i in range(right, left-1, -1):
                if head:
                    res[down][i] = head.val
                    head = head.next
            down -= 1

            for i in range(down, top-1, -1):
                if head:
                    res[i][left] = head.val
                    head = head.next
            
            left += 1

        return res

node2 = ListNode(3)
node3 = ListNode(0)
node4 = ListNode(2)
node5 = ListNode(6)
node6 = ListNode(8)
node7 = ListNode(1)
node8 = ListNode(7)
node9 = ListNode(9)
node10 = ListNode(4)
node11 = ListNode(2)
node12 = ListNode(5)
node13 = ListNode(5)
node14 = ListNode(0)

node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node12
node12.next = node13
node13.next = node14


print(Solution().spiralMatrix(3, 5, node2)) 
