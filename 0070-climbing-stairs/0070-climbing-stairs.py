class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def climb(n):
            if n <= 2:
                return n
            elif mem.get(str(n)):
                return mem[str(n)]
            else:
                left = climb(n-1)
                right = climb(n-2)
                mem[str(n)] = left + right
                return mem[str(n)]
        
        return climb(n)