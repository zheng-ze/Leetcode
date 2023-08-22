import re

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        # Remove all whitespaces at front
        i = 0
        while i + 1 < len(s) and s[i] == ' ':
            i += 1
        
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            i += 1
            sign = -1
        
        j = i
        while j < len(s) and s[j].isnumeric():
            j += 1
        
        # No numeric numbers after spaces
        if (j == i): 
            return 0
            
        num = int(s[i : j]) * sign
        
        int_min = (1 << 31) * -1
        int_max = (1 << 31) - 1
        if num < int_min:
            return int_min
        if num > int_max:
            return int_max
        return num
        
        
        