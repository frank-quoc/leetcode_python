class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        # dummy nodes
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
        added_node = Node(key, value)
        self._add(added_node)
        self.dict[key] = added_node
        if len(self.dict) > self.capacity:
            removed_node = self.tail.prev
            self._remove(removed_node)
            del self.dict[removed_node.key]
    
    def _add(self, node):
        """Adds to the beginning of the DLL as recently used"""
        next_node = self.head.next
        next_node.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        
    def _remove(self, node):
        """Removes node when called or at capacity"""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
