class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"(": ")", "[": "]", "{": "}"}
        
        for c in s:
            if c in dic:
                stack.append(dic[c])
            elif not stack or stack.pop(-1) != c:
                return False
        
        return not stack