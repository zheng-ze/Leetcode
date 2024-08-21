class Solution:
    def minSteps(self, n: int) -> int:
        if n <= 1:
            return 0
        
        result = 0
        
        for i in range(2, n + 1, 1):
            while n % i == 0:
                result += i # Need to paste i number of times
                n /= i
        
        return result