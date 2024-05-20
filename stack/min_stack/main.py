class MinStack:    
    def __init__(self):
        self.stack = []    
        self.min_stack = [] 
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else: 
            current_min_val = self.min_stack[-1]
            if current_min_val > val:
                self.min_stack.append(val)
            else: 
                self.min_stack.append(current_min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
       

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.min_stack[-1]
        

obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
obj.getMin()
obj.pop()
obj.getMin()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()