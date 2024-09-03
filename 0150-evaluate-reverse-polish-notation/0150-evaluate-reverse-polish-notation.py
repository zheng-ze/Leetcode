class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token.isnumeric() or token[0] == '-' and token[1:].isnumeric():
                stack.append(int(token))
                continue
            if token == "+": 
                num2, num1 = stack.pop(), stack.pop()
                
                stack.append(num1 + num2)
            elif token == "-":
                num2, num1 = stack.pop(), stack.pop()
                
                stack.append(num1 + -num2)
            elif token == "*":
                num2, num1 = stack.pop(), stack.pop()
                
                stack.append(num1 * num2)
            else:
                num2, num1 = stack.pop(), stack.pop()
                
                stack.append(int(float(num1)/num2))
        return stack[0]
