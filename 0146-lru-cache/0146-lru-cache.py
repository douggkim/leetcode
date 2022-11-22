class LRUCache:

    def __init__(self, capacity: int):
        # Positive
        self.capacity = capacity 
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        # print(f"get: {key}")
        if key in self.d: 
            self.d[key] = self.d.pop(key)
            return self.d[key]
        else:
            return -1 
        

    def put(self, key: int, value: int) -> None:
        if key not in self.d: 
            if self.capacity <= len(self.d):
                self.d.popitem(last=False)
        else: 
            self.d.pop(key)
            
        self.d[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)