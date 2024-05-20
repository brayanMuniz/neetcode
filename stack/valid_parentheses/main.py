# if open add it to stack
# if close and end of stack matches, pop end of stack 
# is stack is not empty by the end return false
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0:
                    return False
                if stack[len(stack) -1] == "(":
                    stack.pop()
                else: 
                    return False
            elif char == "]":
                if len(stack) == 0:
                    return False
                if stack[len(stack) -1] == "[":
                    stack.pop()
                else: 
                    return False
            elif char == "}":
                if len(stack) == 0:
                    return False
                if stack[len(stack) -1] == "{":
                    stack.pop()
                else: 
                    return False
        
        return len(stack) == 0
        