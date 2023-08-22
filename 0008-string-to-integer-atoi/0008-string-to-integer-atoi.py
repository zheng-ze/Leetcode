import re

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        i = 0
        while i + 1 < len(s) and s[i] == ' ':
            i += 1
            
        if not re.search("^(\\d|\-|\+)+$", s[i]):
            return 0
        
        if not s[i].isnumeric():
            i += 1
        
        j = i
        while j < len(s) and s[j].isnumeric():
            j += 1
            
        if (j == i):
            return 0
            
        num = int(s[i : j])
        print(num)
        
        if s[max(0, i - 1)] == '-':
            return -num if -num > (1 << 31) * -1 else (1 << 31) * -1
        else:
            return num if num < (1 << 31) - 1 else (1 << 31) - 1
        
        
        