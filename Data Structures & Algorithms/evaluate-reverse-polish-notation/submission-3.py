class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                right = stack.pop()
                left = stack.pop()
                # Cast to int to truncate strictly toward zero
                stack.append(int(left / right))
            else:
                # The token is a number
                stack.append(int(token))
                
        return stack[0]