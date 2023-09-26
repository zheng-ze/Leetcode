class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        indices = dict()
        stack = []
        used = set()
        
        for i in range(len(s)):
            indices[s[i]] = i
                    
        for i, c in enumerate(s):
            if c in used:
                continue
            
            # Pop all elements that are smaller lexicographically and exist later on
            while stack and c < stack[-1] and indices[stack[-1]] > i:
                used.remove(stack.pop())
            
            stack.append(c)
            used.add(c)
        
        return "".join(stack)