symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        prev = 0
        curr = 1
        total = 0
        while curr < len(s):
            if symbol[s[prev]] < symbol[s[curr]]:
                total += symbol[s[curr]] - symbol[s[prev]]
                prev = curr + 1
                curr += 2
            else:
                total += symbol[s[prev]]
                prev = curr
                curr += 1
        if curr == len(s):
            total += symbol[s[curr - 1]]
        return total 