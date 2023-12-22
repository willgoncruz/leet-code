class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            c = s[i]
            
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            
            if c == ')':
                top = stack.pop() if stack else ''
                if top != '(':
                    return False
            
            if c == '}':
                top = stack.pop() if stack else ''
                if top != '{':
                    return False
            
            if c == ']':
                top = stack.pop() if stack else ''
                if top != '[':
                    return False

        return len(stack) == 0
