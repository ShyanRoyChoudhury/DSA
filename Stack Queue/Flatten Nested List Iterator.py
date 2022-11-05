"""
Link : https://www.youtube.com/watch?v=Liz73RB-Dqs
"""

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattenedList = []

        def flattened(givenList):
            for i in givenList:
                if i.isInteger():
                    self.flattenedList.append(i.getInteger()) # if integer, then appending in final list
                else:
                    flattened(i.getList())   #  else calling recursion again

        flattened(nestedList) # recursion call

        self.position = 0
        
    def next(self) -> int:
        returnItem = self.flattenedList[self.position]
        self.position = self.position + 1
        return returnItem
    
    def hasNext(self) -> bool:
         return self.position <= len(self.flattenedList) - 1
      
      
   """
   T.C: O(N + L), L is the total number of lists inside nested lists
   S.C: O(N + D), D is the depth of nested list
   """
