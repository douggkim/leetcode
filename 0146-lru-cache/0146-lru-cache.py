class Node: 
    def __init__(self, key, val): 
        self.key = key
        self.val = val 
        self.next = None 
        self.prev = None 
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capa = capacity
        self.dic = {} 
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail 
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.dic: 
            return -1 

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val 

    def put(self, key: int, value: int) -> None:
        if key in self.dic: 
            old_node = self.dic[key]
            self.remove(old_node)
        
        node = Node(key,value)
        self.dic[key] = node 
        self.add(node)

        if len(self.dic) > self.capa: 
            previous = self.head.next 
            self.remove(previous)
            del self.dic[previous.key]
            

    
    def add(self, node): 
        previous = self.tail.prev 
        previous.next = node 
        node.prev = previous
        node.next = self.tail
        self.tail.prev = node 

    def remove(self, node): 
        node.prev.next = node.next 
        node.next.prev = node.prev 

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)