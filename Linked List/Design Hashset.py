class MyHashSet(object):

    def __init__(self):
        self.size = 10000
        self.table = [[None] for _ in range(self.size)]
        #print(self.table)
    def hash(self, key):
        return key%self.size
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = self.hash(key)
        if self.table[i] == None:
            self.table[i] = []
        self.table[i].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = self.hash(key)
        if self.table[i] != None:
            while key in self.table[i]:
                self.table[i].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        i = self.hash(key)
        if self.table[i] != None:
            return key in self.table[i]
        else:
            return False
          
"""
Time Complexity:  O(N) --> In the worst case, we need to search the entire self.table[i] to check if key is present
Space Complexity: O(N) --> We use a self.table[] to store all the Unique Keys
"""
