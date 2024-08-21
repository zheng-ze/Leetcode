class Solution:
    def minSteps(self, n: int) -> int:
        if n <= 1:
            return 0
                
        def helper(savedLength: int, currLength: int, currOperations: int) -> int:
            if currLength == n:
                return 0
            
            if currLength > n:
                return float('inf')
            
                        
            if currOperations & 1 == 0:
                return 1 + helper(currLength, currLength + savedLength, currOperations << 1 | 1)
            
            return 1 + min(helper(savedLength, currLength + savedLength, currOperations << 1 | 1), helper(currLength, currLength, currOperations << 1))
        
        return 1 + helper(1, 1, 0)