class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        indices = dict()
        stack = []
        length = len(s)
        used = set()
        
        for i in range(length):
            indices[s[i]] = i
                    
        for i in range(length):
            if s[i] in used:
                continue
            
            # Pop all elements that are smaller lexicographically and exist later on
            while stack and s[i] < stack[-1] and indices[stack[-1]] > i:
                used.remove(stack.pop())
            
            stack.append(s[i])
            used.add(s[i])
        
        return "".join(stack)