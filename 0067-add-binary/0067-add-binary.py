class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        temp = 0
        output = ""
        
        while (a and b) or temp:
            if a:
                temp += int(a.pop())
            if b:
                temp += int(b.pop())
            if temp < 2:
                output = str(temp) + output
                temp = 0
            else:
                output = str(temp % 2) + output
                temp = 1
        if a:
            output = ''.join(str(x) for x in a) + output
        if b:
            output = ''.join(str(x) for x in b) + output
            
        return output