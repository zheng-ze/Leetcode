class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        denominator = 1
        
        i = 0
        length = len(expression)
        while i < length:
            curr_numerator = 0
            curr_denominator = 0
            
            sign = 1
            
            if expression[i] == '-':
                sign = -1
            
            if not expression[i].isnumeric():
                i += 1
            
            while i < length and expression[i].isnumeric():
                curr_numerator = curr_numerator * 10 + int(expression[i])
                i += 1
        
            i += 1
            
            while i < length and expression[i].isnumeric():
                curr_denominator = curr_denominator * 10 + int(expression[i])
                i += 1
            
            numerator = numerator * curr_denominator + curr_numerator * denominator * sign
            denominator *= curr_denominator
            
        gcd = abs(math.gcd(numerator, denominator))
        
        numerator //= gcd
        denominator //= gcd
        
        return f"{numerator}/{denominator}" 
                
