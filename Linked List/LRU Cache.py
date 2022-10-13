class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    # create hasmap and it's capacity, doubly with lru == head, mru == tail
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap={}

        self.lru = Node(0,0)    # Dll creation | head, tail
        self.mru = Node(0,0)

        self.lru.next = self.mru    # assigning pointers
        self.mru.prev = self.lru

    def remove(self, Node):     # removes the node
        nextNode, prevNode = Node.next, Node.prev
        nextNode.prev, prevNode.next = prevNode, nextNode
    
    def insert(self, Node):     # insert at MRU
        prev = self.mru.prev
        prev.next = Node
        Node.prev = prev
        self.mru.prev = Node
        Node.next = self.mru
    
    # return the cache's val withh the key | Updates the order of cache -> removes the node and link it to MRU
    def get(self, key: int) -> int:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
            self.insert(self.cacheMap[key])
            return self.cacheMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
            del self.cacheMap[key]

        self.cacheMap[key] = Node(key, value)       # storing new node to the cacheMap
        self.insert(self.cacheMap[key])     # link to the DLL
        
        # if insertion excedes the capacity then update the DLL
        if len(self.cacheMap) > self.capacity:
            lruNode = self.lru.next
            self.remove(lruNode)
            del self.cacheMap[lruNode.key]
            
"""
Tc : O(1)
Sc : O(capacity)
"""
