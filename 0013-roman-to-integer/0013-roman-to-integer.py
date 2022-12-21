class Solution:
    def romanToInt(self, s: str) -> int:
        prev = ""
        total = 0
        symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for c in s:
            total += symbol[c]
            if prev == "I" and (c == "V" or c == "X"):
                total -= 2
            if prev == "X" and (c == "L" or c == "C"):
                total -= 20
            if prev == "C" and (c == "D" or c == "M"):
                total -= 200
            prev = c
            print(total)
        return total