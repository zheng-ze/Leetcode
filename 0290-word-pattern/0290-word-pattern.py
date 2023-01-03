class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(" ")
        return len(set(zip(pattern, list_s))) == len(set(pattern)) == len(set(list_s)) and len(list_s) == len(pattern)
