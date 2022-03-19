class FreqStack:

    def __init__(self):
        self.stack = {}
        self.count = {}
        self.maxCount = 0
            
    def push(self, val: int) -> None:
        valcount = 1 + self.count.get(val, 0)
        self.count[val] = valcount
        if valcount > self.maxCount:
            self.maxCount = valcount
            self.stack[valcount] = []
        self.stack[valcount].append(val) 

    def pop(self) -> int:
        data = self.stack[self.maxCount].pop()
        self.count[data] -= 1
        if not self.stack[self.maxCount]:
            self.maxCount -= 1
        return data

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()