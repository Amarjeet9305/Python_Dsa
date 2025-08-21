class MinStack:
    def __init__(self):
        self.stack = []      # Normal stack
        self.minStack = []   # Stack to keep track of mins

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push min(val, last min) to minStack
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
# Driver Code
obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)

print(obj.getMin())  # 0
obj.pop()
print(obj.getMin())  # 0
obj.pop()
print(obj.getMin())  # 0
obj.pop()
print(obj.getMin())  # 2
