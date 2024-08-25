class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")": "(", "]": "[", "}": "{"}
        
        for c in s:
            if c not in dic:
                stack.append(c)
                continue
            
            if not stack or stack[-1] != dic[c]:
                return False
            
            stack.pop(-1)
        
        return not stack