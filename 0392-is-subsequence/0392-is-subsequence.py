class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        length = len(t)
        for char in s:
            while i < length and t[i] != char:
                i += 1
            
            if i >= length:
                return False
            
            i += 1
        
        return True