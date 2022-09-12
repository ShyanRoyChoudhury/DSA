class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def search(i, j, m, n, k):
          # If k is equal to the given word's length, it means every character of word is present inside board[][], so we return true

            if k == len(word):
                return True
              # If we are moving outside the board's boundary or if board[i][j] is not equal to word[k] , we return false
            if i < 0 or j < 0 or i == m or j == n or board[i][j] != word[k]:
                return False
            ch = board[i][j]  # We store the Character present in the current Cell inside ch variable
            board[i][j] = "#" # We change board[i][j] to # so that we don't visit the Same Cell again
            op1 = search(i+1, j, m, n, k+1)
            op2 = search(i-1, j, m, n, k+1)
            op3 = search(i, j+1, m, n, k+1)
            op4 = search(i, j-1, m, n, k+1)
            board[i][j] = ch    # backtracking
            return op1 or op2 or op3 or op4
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):        
                if board[i][j] == word[0]:  #if the first letter matches the first letter of the input.
                    if search(i, j, m, n, 0):
                        return True
        
        return False
      
"""
Time Complexity:  O(N * M * 4^K)
Space Complexity: O(K) | k = len(word)
"""
