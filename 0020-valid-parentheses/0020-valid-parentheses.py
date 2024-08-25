class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif len(stack) == 0 or stack.pop(-1) != c:
                return False
        
        return len(stack) == 0