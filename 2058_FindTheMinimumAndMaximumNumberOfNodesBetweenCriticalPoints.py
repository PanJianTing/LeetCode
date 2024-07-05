class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        cur = head
        pre_node = None
        next_node = head.next
        critical_list = []
        idx = 0

        while next_node:
            if pre_node and next_node:
                if pre_node.val < cur.val and next_node.val < cur.val:
                    critical_list.append(idx)
                elif pre_node.val > cur.val and next_node.val > cur.val:
                    critical_list.append(idx)
            pre_node = cur
            cur = next_node
            next_node = next_node.next
            idx += 1
        
        N = len(critical_list)
        if N < 2:
            return [-1, -1]
        min_dis = float('inf')
        max_dis = critical_list[-1] - critical_list[0]
        
        for i in range(1, N):
            min_dis = min(min_dis, critical_list[i] - critical_list[i-1])
        
        return [min_dis, max_dis]
    
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        cur = head
        pre_node = None
        next_node = head.next
        idx = 0
        pre_idx = None
        first_idx = None
        min_dist = float('inf')
        max_dist = 0

        while next_node:
            if pre_node and next_node:
                if (pre_node.val < cur.val and next_node.val < cur.val) or (pre_node.val > cur.val and next_node.val > cur.val):
                    if first_idx:
                        min_dist = min(min_dist, idx - pre_idx)
                        max_dist = idx - first_idx
                        pre_idx = idx
                        
                    else:
                        first_idx = idx
                        pre_idx = idx
                        
                    
            pre_node = cur
            cur = next_node
            next_node = next_node.next
            idx += 1
        
        if min_dist == float('inf'):
            return [-1, -1]
        
        return [min_dist, max_dist]