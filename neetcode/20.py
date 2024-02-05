# valid parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        
        for c in s:
            if c in closeToOpen: #check if c is a closing parenthesis
                #check if stack is not empty and top element is opening parenthesis for c
                if stack and stack[-1] == closeToOpen[c]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        # check if the stack is empty indicating that the stack is valid
        return True if not stack else False