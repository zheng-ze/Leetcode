class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ""
        
        while columnNumber > 0:
            columnNumber -= 1

            curr = columnNumber % 26
            
            out = chr(curr + 65) + out
        
            columnNumber //= 26
        
        return out