from collections import defaultdict

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
    

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        cnt_map = defaultdict(list)
        cur = head
        idx = 0
        
        while cur:
            cnt_map[cur.val].append(idx)
            cur = cur.next
            idx += 1

        idx_cnt_list = []
        for k, idx_list in cnt_map.items():
            if len(idx_list) == 1:
                idx_cnt_list.append((idx_list[0], k))

        idx_cnt_list.sort()
        res = ListNode(-1)
        cur = res

        for i in range(len(idx_cnt_list)):
            _, cnt = idx_cnt_list[i]
            cur.next = ListNode(cnt)
            cur = cur.next
        return res.next

    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        cnt_map = defaultdict(int)
        cur = head

        while cur:
            cnt_map[cur.val] += 1
            cur = cur.next

        dummy = ListNode(-1)
        res = dummy
        cur = head

        while cur:
            if cnt_map[cur.val] == 1:
                dummy.next = ListNode(cur.val)
                dummy = dummy.next
            cur = cur.next
        return res.next
    

    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        cnt_map = defaultdict(int)
        temp = head
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy.next
        pre = dummy

        while temp:
            cnt_map[temp.val] += 1
            temp = temp.next
        
        while cur:
            if cnt_map[cur.val] > 1:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next
    
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        cnt_map = defaultdict(int)

        def countFreq(cur):
            while cur:
                cnt_map[cur.val] += 1
                cur = cur.next
        
        def helper(cur):
            if cur == None:
                return cur
            nextNode = helper(cur.next)
            cur.next = nextNode
            if cnt_map[cur.val] > 1:
                return nextNode
            else:
                return cur
            
        countFreq(head)
        return helper(head)

        