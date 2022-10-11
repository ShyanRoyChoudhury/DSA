class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap={}

        self.lru = Node(0,0)
        self.mru = Node(0,0)

        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove(self, Node):
        nextNode, prevNode = Node.next, Node.prev
        nextNode.prev, prevNode.next = prevNode, nextNode

    def insert(self, Node):
        prev = self.mru.prev
        prev.next = Node
        Node.prev = prev
        self.mru.prev = Node
        Node.next = self.mru

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

        self.cacheMap[key] = Node(key, value)
        self.insert(self.cacheMap[key])

        if len(self.cacheMap) > self.capacity:
            lruNode = self.lru.next
            self.remove(lruNode)
            del self.cacheMap[lruNode.key]
