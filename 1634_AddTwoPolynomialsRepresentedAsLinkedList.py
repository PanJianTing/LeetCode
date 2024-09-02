from collections import defaultdict

class PolyNode:
    def __init__(self, x = 0, y = 0, next = None) -> None:
        self.coefficient = x
        self.power = y
        self.next = next
        return


class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = PolyNode()
        cur = dummy

        while poly1 and poly2:
            if poly1.power > poly2.power:
                temp = PolyNode(poly1.coefficient, poly1.power)
                cur.next = temp
                cur = cur.next
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                temp = PolyNode(poly2.coefficient, poly2.power)
                cur.next = temp
                cur = cur.next
                poly2 = poly2.next
            else:
                if poly1.coefficient + poly2.coefficient != 0:
                    temp = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power)
                    cur.next = temp
                    cur = cur.next

                poly1 = poly1.next
                poly2 = poly2.next
        if poly1:
            cur.next = poly1
        if poly2:
            cur.next = poly2
        return dummy.next

    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        key_map = defaultdict(int)

        def set_coefficient(cur):
            while cur:
                key_map[cur.power] += cur.coefficient
                cur = cur.next

        set_coefficient(poly1)
        set_coefficient(poly2)

        dummy = PolyNode()
        cur = dummy

        for k in sorted(key_map.keys(), reverse=True):
            if key_map[k] == 0:
                continue
            temp = PolyNode(key_map[k], k)
            cur.next = temp
            cur = cur.next
        return dummy.next
    
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = PolyNode()
        cur = dummy

        while poly1 and poly2:
            if poly1.power > poly2.power:
                cur.next = poly1
                cur = cur.next
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                cur.next = poly2
                cur = cur.next
                poly2 = poly2.next
            else:
                if poly1.coefficient + poly2.coefficient != 0:
                    temp = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power)
                    cur.next = temp
                    cur = cur.next

                poly1 = poly1.next
                poly2 = poly2.next
        
        if poly1:
            cur.next = poly1
        else:
            cur.next = poly2
        return dummy.next