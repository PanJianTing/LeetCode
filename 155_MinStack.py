class MinStack:

    stack = []
    temp = []

    def __init__(self):
        self.stack = []
        self.temp = [float('inf')]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.temp[-1] >= val:
            self.temp.append(val)
        

    def pop(self) -> None:
        temp_pop = self.stack.pop()
        if self.temp[-1] == temp_pop:
            self.temp.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.temp[-1]

class MinStack_my:

    stack = []
    sortStack = []

    def __init__(self):
        self.stack = []
        self.sortStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.sortStack = sorted(self.stack, reverse=True)
        

    def pop(self) -> None:
        self.stack.pop()
        self.sortStack = sorted(self.stack, reverse=True)

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.sortStack[-1]



stack = MinStack()

["MinStack","push","push","push","getMin","pop","top","getMin"]
print(stack.push(-2))
print(stack.push(0))
print(stack.push(-3))

print(stack.getMin())
print(stack.pop())
print(stack.top())
print(stack.getMin())

