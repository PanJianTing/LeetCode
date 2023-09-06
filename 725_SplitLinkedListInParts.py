class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head, k):
        ans = []
        N = 0
        ptr = head
        
        while ptr:
            N += 1
            ptr = ptr.next
        
        cnt = N // k
        leave = N % k

        ptr = head

        while ptr:
            temp_ptr = ptr
            idx = 0
            needCnt = cnt
            if leave > 0:
                needCnt += 1
                leave -= 1
            while idx < needCnt:
                if idx == needCnt - 1:
                    temp = ptr
                    ptr = ptr.next
                    temp.next = None
                else:
                    ptr = ptr.next

                idx += 1
            ans.append(temp_ptr)
        
        while len(ans) < k:
            ans.append(None)
            
        return ans
    
    def splitListToParts(self, head, k):
        N = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            N += 1
        
        cnt = N // k
        remain = N % k
        ans = []

        ptr = head
        for _ in range(k):
            cur = ListNode(0)
            tempHead = cur
            partCnt = cnt
            if remain > 0:
                partCnt += 1
                remain -= 1
            
            for _ in range(partCnt):
                cur.next = ListNode(ptr.val)
                cur = cur.next
                ptr = ptr.next
                
            ans.append(tempHead.next)
        
        return ans
    
    def splitListToParts(self, head, k):
        N = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            N += 1

        cnt = N // k
        remain = N % k
        
        ans = []
        ptr = head
        for i in range(k):
            temp = ptr
            partcnt = cnt + (1 if i < remain else 0)
            for _ in range(partcnt-1):
                if ptr:
                    ptr = ptr.next
            
            if ptr:
                h = ptr
                ptr = ptr.next
                h.next = None
            ans.append(temp)

        return ans
            
    

print("Case 1")
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

ansList = Solution().splitListToParts(node1, 5)


for head in ansList:
    while head:
        print(head.val)
        head = head.next
    print("=====")

print("Case 2")


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)
node10 = ListNode(10)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

ansList = Solution().splitListToParts(node1, 3)


for head in ansList:
    while head:
        print(head.val)
        head = head.next
    print("=====")