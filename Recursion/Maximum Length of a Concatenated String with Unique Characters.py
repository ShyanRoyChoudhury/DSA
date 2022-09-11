class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def compare(currString):
            selfCheck = [0 for i in range(26)]
            
            a = ord("a")
            for i in currString:            #check for duplicates in current String
                if selfCheck[ord(i)-a] == 1:
                    return False
                
                selfCheck[ord(i)-a] = 1
                
            for i in currString:    #checks whether the characters of current String are already in selected
                if selected[ord(i) - a] == 1:
                    return False
                
            return True
        
        def help(i, length):
            
            #base condition
            if i == len(arr):
                return length
            a = ord("a")
            currString = arr[i]
            
            if compare(currString) == False:
                return help(i+1, length)
            else:
                #pick
                for ch in currString:
                    selected[ord(ch)-a] = 1
                
                length += len(currString)
                
                op1 = help(i+1, length)   #recursion
                
                #skip
                for j in currString:
                    selected[ord(j)-a]  = 0   #backtracking
                length -= len(currString)       #backtracking
                
                op2 = help(i+1, length)
                
                return max(op1, op2)
            
        selected = [0 for i in range(26)] 
        
        return help(0,0)
