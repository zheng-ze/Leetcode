class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = list(Counter(s).items())
        length = 0
        odd = False
        for item in count:
            x, n = item
            length += (n - (n % 2))
            if n % 2 == 1:
                odd = True
            
        return length + 1 if odd else length
