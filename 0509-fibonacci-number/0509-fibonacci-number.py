class Solution:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        if n in self.mem:
            return self.mem[n]

        ans = self.fib(n - 1) + self.fib(n - 2)
        self.mem[n] = ans
        
        return ans

