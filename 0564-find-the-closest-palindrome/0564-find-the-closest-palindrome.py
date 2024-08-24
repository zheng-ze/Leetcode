class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length, num = len(n), int(n)
        
        if length <= 1:
            return str(num - 1)
        
        mid = length // 2 if length % 2 == 0 else length // 2 + 1
        prefix = int(n[:mid])
        
        possible = []
        
        def build_palindrome(prefix: int) -> str:
            p = str(prefix)
            return p + (p[:-1] if length % 2 else p)[::-1]
        
        possible.extend(["9" * (length - 1), "1" + "0" * (length - 1) + "1"])
        possible.extend(map(build_palindrome, [prefix - 1, prefix, prefix + 1]))
        
        return min(possible, key = lambda candidate: abs(num - int(candidate)) or float('inf'))