class MyHashSet:

    def __init__(self):
        self.hashSet = set([])

    def add(self, key):
        self.hashSet.add(key)

    def remove(self, key):
        if key in self.hashSet:
            self.hashSet.remove(key)

    def contains(self, key):
        if key in self.hashSet:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)