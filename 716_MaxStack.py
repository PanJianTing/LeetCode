class MaxStack:

    stack = []
    maxValue = float("-inf")


    def __init__(self) -> None:
        self.stack = []
        self.maxValue = float("-inf")


    def push(self, x: int) -> None:
        self.stack.append(x)
        if x > self.maxValue:
            self.maxValue = x

    def pop(self) -> int:
        popNum = self.stack.pop()
        if popNum == self.maxValue:
            if self.stack == []:
                self.maxValue = float("-inf")
            else:
                self.maxValue = max(self.stack)
        return popNum

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxValue

    def popMax(self) -> int:
        maxValue = self.peekMax()
        
        for i in range(len(self.stack)- 1, -1, -1):
            if self.stack[i] == maxValue:
                self.stack.pop(i)
                break
        
        if self.stack == []:
            self.maxValue = float("-inf")
        else:
            self.maxValue = max(self.stack)

        return maxValue

class MaxStack_k:

    stack = []
    stackMax = []

    def __init__(self) -> None:
        self.stack = []
        self.stackMax = [float("-inf")]

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if x >= self.stackMax[-1]:
                self.stackMax.append(x)

    def pop(self) -> int:
        popVal = self.stack.pop()
        if popVal == self.stackMax[-1]:
            self.stackMax.pop()
        return popVal

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.stackMax[-1]

    def popMax(self) -> int:
        maxValue = self.stackMax.pop()

        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == maxValue:
                self.stack.pop(i)
                break
        for j in range(i, len(self.stack)):
            if self.stack[j] >= self.stackMax[-1]:
                self.stackMax.append(self.stack[j])
        return maxValue

class MaxStack_1:

    stack = []

    def __init__(self) -> None:
        self.stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        maxValue = self.peekMax()

        for i in range(len(self.stack)- 1, -1, -1):
            if self.stack[i] == maxValue:
                return self.stack.pop(i)


class MaxStack_my:

    stack = []
    stackMax = []


    def __init__(self) -> None:
        self.stack = []
        self.stackMax = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        self.stackMax.append(max(self.stack))

    def pop(self) -> int:
        popNum = self.stack.pop()
        self.stackMax.pop()
        return popNum

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.stackMax[-1]

    def popMax(self) -> int:
        maxValue = self.peekMax()
        
        buffer = []

        while self.top() != maxValue: buffer.append(self.pop())
        self.pop()
        
        for i in range(len(buffer) - 1, -1, -1):
            self.push(buffer[i])

        return maxValue


testStack = MaxStack()


["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]
[[],[5],[1],[5],[],[],[],[],[],[]]
testStack.push(5)
testStack.push(1)
testStack.push(5)
print(testStack.top())
print(testStack.popMax())
print(testStack.top())
print(testStack.peekMax())
print(testStack.pop())
print(testStack.top())



# ["MaxStack","push","push","popMax","peekMax"]
# [[],[5],[1],[],[]]


# testStack.push(5)
# testStack.push(1)
# print(testStack.popMax())
# print(testStack.peekMax())



# ["MaxStack","push","push","push","popMax","popMax","top"]
# [[],[5],[1],[-5],[],[],[]]



# testStack.push(5)
# testStack.push(1)
# testStack.push(-5)
# print(testStack.popMax())
# print(testStack.popMax())
# print(testStack.top())


# ["MaxStack","push","push","top","popMax","push","peekMax","push","pop","pop","popMax","push","push","top","popMax"]
# [[],[-2],[8],[],[],[64],[],[3],[],[],[],[87],[-88],[],[]]

# print(testStack.push(-2))
# print(testStack.push(8))
# print(testStack.top())
# print(testStack.popMax())
# print(testStack.push(64))
# print(testStack.peekMax())
# print(testStack.push(3))
# print(testStack.pop())
# print(testStack.pop())
# print(testStack.popMax())
# print(testStack.push(87))
# print(testStack.push(-88))
# print(testStack.top())
# print(testStack.popMax())