import random

class ListNode:
    def __init__(self, val= 0, next= None) -> None:
        self.val = val
        self.next = next

class Solution:
    allVal = []
    allCount = 0
    def __init__(self, head: ListNode):
        self.allVal = []

        while head:
            self.allVal.append(head.val)
            head = head.next

        self.allCount = len(self.allVal)

    def getRandom(self) -> int:
        pick = random.randint(0, (self.allCount - 1))
        return self.allVal[pick]