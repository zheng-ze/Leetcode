class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None or val < self.min:
            self.min = val
        self.stack.append((val, self.min))

    def pop(self) -> None:
        self.stack.pop()
        
        if not self.stack:
            self.min = None
            return
        
        if self.min < self.stack[-1][1]:
            self.min = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()