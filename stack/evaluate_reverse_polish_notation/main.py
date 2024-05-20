# https://en.wikipedia.org/wiki/Reverse_Polish_notation
# post-fix notation converter 
# have a stack that has the operands 
# if you encounter an operator, evaluate and return the value to the stack 
# at the end you have a single value in the stack, return that

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "-", "*", "/"]
        for t in tokens: 
            if t not in operands:
                stack.append(t)
            else:
                val = None
                if t == "+":
                    val = int(stack[-2]) + int(stack[-1])
                elif t == "-":
                    val = int(stack[-2]) - int(stack[-1])
                elif t == "*":
                    val = int(stack[-2]) * int(stack[-1])
                else:
                    val = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)
        return int(stack[0])
    
x = Solution()
print(x.evalRPN(["4","13","5","/","+"]))