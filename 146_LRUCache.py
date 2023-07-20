from collections import defaultdict, deque, OrderedDict

class ListNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:
    cap = {}
    cnt = 0
    head = None
    tail = None

    def __init__(self, capacity) -> None:
        self.cap = {}
        self.cnt = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        return

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        return

    def add(self, node):
        endTail = self.tail.pre
        endTail.next = node
        node.pre = endTail
        node.next = self.tail
        self.tail.pre = node
        return

    def get(self, key) -> int:
        if key in self.cap:
            node = self.cap[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1
        
    def put(self, key, value) -> None:
        if key in self.cap:
            oldNode = self.cap[key]
            self.remove(oldNode)
        
        newNode = ListNode(key, value)
        self.cap[key] = newNode
        self.add(newNode)

        if len(self.cap) > self.cnt:
            deleteNode = self.head.next
            self.remove(deleteNode)
            del self.cap[deleteNode.key]
        return
    
class LRUCache:
    cnt = 0
    dic = OrderedDict()

    def __init__(self, cap) -> None:
        self.cnt = cap
        self.dic = OrderedDict()

    def get(self, key) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        return -1
    
    def put(self, key, value) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        
        self.dic[key] = value
        if len(self.dic) > self.cnt:
            self.dic.popitem(False)
        return

     