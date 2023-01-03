class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        return len(set(zip(pattern, s))) == len(set(pattern)) == len(set(s)) and len(s) == len(pattern)
