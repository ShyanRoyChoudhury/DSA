def searchMaze(arr, n):
    def help(i, j,n):
        if i<0 or j<0 or i==n or j==n or arr[i][j]==0:
            return
        elif i==n-1 and j==n-1:
            ans.append("".join(path))
            return
        else:
            arr[i][j]=0
            
            path.append('D')      # NOTE: FOLLOW THIS SPECIFIC SEQUENCE.
            help(i+1,j,n)
            path.pop()
            
            path.append('L')
            help(i,j-1,n)
            path.pop()
            
            path.append('R')
            help(i,j+1,n)
            path.pop()
            
            path.append('U')
            help(i-1,j,n)
            path.pop()
            
            arr[i][j] = 1
    
    ans=[]
    path=[]
    help(0,0,n)
    return ans
  
  
"""
Time Complexity: O(4^(N * N) )
Space Complexity: O(N * N)
"""
