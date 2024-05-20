# Only add open if open < n 
# Only add closed if closed < open 
# if open == closed == n return 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def back_track(amount_open, amount_closed):
            if amount_open == amount_closed == n:
                result.append("".join(stack))
                return

            if amount_open < n:
                stack.append("(")
                back_track(amount_open + 1, amount_closed)
                stack.pop()
            
            if amount_closed < amount_open:
                stack.append(")")
                back_track(amount_open, amount_closed + 1)
                stack.pop()
            
        back_track(0,0)                
        return result
            