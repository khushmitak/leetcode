#design a stack that supports push, pop, top, and retrieving the minimum element in constant time

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        #push the value in a stack by appending it
        self.stack.append(val)
        #for minStack, check if the minStack is empty or not
        if self.minStack: #if the minStack is non-empty, compare the value with top element's value and get the min
            val = min(val, self.minStack[-1])
        else: #if the minStack is empty, just push the value in minStack
            val = val
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        