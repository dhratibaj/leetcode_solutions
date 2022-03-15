class stack:
    def __init__(self):
        self.Stack = []
    
    def push(self,val):
        self.Stack.append(val)
    def pop(self):
        return self.Stack.pop()
    def isEmpty(self):
        if len(self.Stack)==0:
            return True
        return False
    
class MyQueue:

    def __init__(self):
        self.stacks = stack()
        self.temp = stack()
        
    def push(self, x: int) -> None:
        self.stacks.push(x)
        
    def pop(self) -> int:
        if not self.temp.isEmpty():
            return self.temp.pop()
        else:
            while not self.stacks.isEmpty():
                self.temp.push(self.stacks.pop())
            return self.temp.pop()
        return self.stacks.pop()
    
    def peek(self) -> int:
        if not self.temp.isEmpty():
            return self.temp.Stack[-1]
        else:
            while not self.stacks.isEmpty():
                self.temp.push(self.stacks.pop())
            return self.temp.Stack[-1]
        
    def empty(self) -> bool:
        return self.stacks.isEmpty() and self.temp.isEmpty()
    
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
