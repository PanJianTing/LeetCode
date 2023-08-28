from collections import deque

class MyStack:
    def __init__(self) -> None:
        self.q = deque()

    def push(self, x) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
    
class MyStack:
    def __init__(self) -> None:
        self.q1 = deque()
        self.q2 = deque()
        self.myTop = 0
    
    def push(self, x):
        self.q1.append(x)
        self.myTop = x
    
    def pop(self):
        while len(self.q1) > 1:
            self.myTop = self.q1.popleft()
            self.q2.append(self.myTop)
        remove = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return remove

    def top(self):
        return self.myTop
    
    def empty(self):
        return len(self.q1) == 0
    

class MyStack():

    def __init__(self) -> None:
        self.q1 = deque()
        self.q2 = deque()
        self.myTop = 0
        pass

    def push(self, x):
        self.q2.append(x)
        self.myTop = x
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        res = self.q1.popleft()
        if self.q1:
            self.myTop = self.q1[0]
        return res

    def top(self):
        return self.myTop

    def empty(self):
        return len(self.q1) == 0
    
class MyStack:

    def __init__(self) -> None:
        self.q = deque()
        self.myTop = 0
    
    def push(self, x):
        size = len(self.q)
        self.q.append(x)
        self.myTop = x
        
        while size > 0:
            self.q.append(self.q.popleft())
            size -= 1
        
    def pop(self):
        res = self.q.popleft()
        if len(self.q):
            self.myTop = self.q[0]

        return res
    
    def top(self):
        return self.myTop
    
    def empty(self):
        return len(self.q) == 0

    
ms = MyStack()
ms.push(1)
ms.push(2)
print(ms.top())
print(ms.pop())
print(ms.empty())


