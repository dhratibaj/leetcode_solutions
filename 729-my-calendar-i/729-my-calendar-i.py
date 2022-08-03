class MyCalendar:

    def __init__(self):
        self.l = []

    def book(self, start: int, end: int) -> bool:
        # print(self.l)
        if self.l == []:
            self.l.append([start,end])
            return True
        else:
            for i,j in self.l:
                if i < end and start < j:
                    return False
            self.l.append([start,end])
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)