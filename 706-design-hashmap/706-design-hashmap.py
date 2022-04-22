class MyHashMap:

    def __init__(self):
        self.temp= {}

    def put(self, key: int, value: int) -> None:
        self.temp[key]= value

    def get(self, key: int) -> int:
        if key in self.temp: return self.temp.get(key)
        else: return -1

    def remove(self, key: int) -> None:
        if key in self.temp: del self.temp[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)