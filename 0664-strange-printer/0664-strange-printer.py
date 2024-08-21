class Solution:
    def strangePrinter(self, s: str) -> int:
        # Simplify string
        s = "".join(a for a, b in zip(s, "_" + s) if a != b)
        mem = {}
        
        def helper(start, end) -> int:
            if start > end:
                return 0
            
            if (start, end) in mem:
                return mem[(start, end)]
            
            turns = 1 + helper(start + 1, end)
            
            for i in range(start + 1, end + 1):
                if s[i] != s[start]: 
                    continue
                # Found duplicate. Can be printed in same time so avoid searching for it.
                turns = min(turns, helper(start, i - 1) + helper(i + 1, end))
                
            mem[(start, end)] = turns
            return turns
        
        return helper(0, len(s) - 1)