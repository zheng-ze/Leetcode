class MyStack:
    """
    Idea to keep the front of the queue as the top of the stack.
    Hence, we need to insert to the front of the queue.
    However, we since, we are limited to the queue operations which only allows us to
    insert to the back of the queue. Hence, we need to move all elements to the back
    
    Complexities:
    Time = O(n) for insert, O(1) for everything else
    Space = O(n)
    """
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        
        
    def pop(self) -> int:
        return self.queue.popleft() # poll

    def top(self) -> int:
        return self.queue[0] # peek
        

    def empty(self) -> bool:
        return len(self.queue) == 0 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()