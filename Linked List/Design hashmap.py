
class MyHashMap(object):
    
    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def Hash(self,key):
        return key%self.size

    def getIndex(self,key):
        hashr = self.Hash(key)
        Maps = self.map[hashr]

        for i,(k,v) in enumerate(Maps):
            if k == key:
                return Maps,i
        return Maps,-1

    def put(self, key, value):
        Maps,idx = self.getIndex(key)

        if idx<0:
            Maps.append((key,value))
        else:
            Maps[idx] = (key,value)

    def get(self, key):
        Maps,idx = self.getIndex(key)
        if idx<0:
            return -1
        else:
            return Maps[idx][1]


    def remove(self, key):
        Maps,idx = self.getIndex(key)
        if idx<0:
            return
        else:
            Maps.remove(Maps[idx])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

'''
Time Complexity:  O(N) --> In the worst case, we need to search the entire m[i] to check if key is present
Space Complexity: O(N) --> We use a List of Lists [[]] to store the {key , value} pairs
'''
