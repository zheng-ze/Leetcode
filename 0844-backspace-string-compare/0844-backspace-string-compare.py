import itertools

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        
        for char_s, char_t in itertools.zip_longest(s, t):
            if char_s == "#":
                if stack1: stack1.pop()
            elif char_s != None:
                stack1.append(char_s)
            if char_t == "#":
                if stack2: stack2.pop()
            elif char_t != None:
                stack2.append(char_t)
        return stack1 == stack2