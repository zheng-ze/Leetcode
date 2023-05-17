class Solution:
    def __init__(self):
        self.mem = {}
        self.mem[2] = 1

    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        
        if n in self.mem:
            return self.mem[n]

        ans = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.mem[n] = ans
        
        return ans