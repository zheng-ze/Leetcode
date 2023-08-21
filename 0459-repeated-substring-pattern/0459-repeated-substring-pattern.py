class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # For all substring with length that can evenly divide,
        # Check if repeating them to length of s makes them s.
        # Do not check for substrings that cannot evenly divide as there is no way to become s.
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                if s[:i] * (len(s) // i) == s:
                    return True
        
        return False
