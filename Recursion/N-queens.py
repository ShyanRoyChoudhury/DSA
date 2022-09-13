"""
/* This problem asks us to fill N Queens in N * N ChessBoard such that no Queen will cancel each other
In order to be sure, no Queen cancel out each other, we need to check in 3 directions:
a) In the column where we are placing the Queen
b) In the Top Right / Upper Right Diagonal of the Cell in which we are placing the Queen
c) In the Top Left  / Upper Left Diagonal of the  Cell in which we are placing the Queen
We don't need to check for the Rows, as each row will contain only a single Queen
Instead of using isSafe() function, which takes O(N) time to check if the Current Cell (i , j) is Safe or Not, we will use 3 vectors:
i)   col[n] --> Checks if we have already placed a Queen or not in the Same Column
ii)  topLeft[2 * n] -->  Checks if our Queen can be attacked by any Queen sitting in it's Top Left Diagonal / Upper Left Diagonal
iii) topRight[2 * n] --> Checks if our Queen can be attacked by any other Queen sitting in it's Top Right Diagonal / Upper Right Diagonal
To mark every index in our topLeft[] & topRight[] vectors, we use the following :
a) For any cell in our ChessBoard (i , j) to map it with corresponsing index in topLeft[], we use the formula: (i - j + n - 1)
b) For any cell in our ChessBoard (i , j) to map it with the corresponding index in topRight[], we use the formula(i + j)
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def help(i,n):
            
            #base condition
            if i == n:
                temp = []
                for j in range(n):
                    currRow = ""
                    for k in range(n):
                        currRow += chessBoard[j][k]
                    temp.append(currRow)
                    
                ans.append(temp[:])
                return
            
            for j in range(n):
                if col[j] == 0 and topLeft[i - j + n -1] == 0 and topRight[i+j] == 0:
                    chessBoard[i][j] = "Q"
                    
                    col[j] = 1
                    topLeft[i - j + n - 1] = 1
                    topRight[i + j] = 1
                    
                    help(i+1, n)
                    chessBoard[i][j] = "."
                    
                    col[j] = 0
                    topLeft[i - j + n - 1] = 0
                    topRight[i + j] = 0
                
        ans = []
        chessBoard = [["." for i in range(n)] for j in range(n)]
        col = [0 for i in range(n)]
        topRight = [0 for i in range(2*n)]
        topLeft = [0 for i in range(2*n)]
        help(0, n)
        
        return ans
        

"""
Time Complexity:  O(N!)
Space Complexity: O(N) {For Recursive Stack and For the 3 arrays col[] , topLeft[] , topRight[] we are using in place of isSafe() function } & O(N^2) {For our ans}
"""
