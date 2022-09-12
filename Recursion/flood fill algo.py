class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def flood(i, j, m, n):
          if i<0 or j<0 or i == m or j == n or image[i][j] != oldColor:  # If we move out of the Matrix Or oldColor is not equal to Color, we return back
            return
          image[i][j] = color   # We change the color of the Current-Cell to newColor
          flood(i+1, j, m, n)   # Recursive call in Downward direction
          flood(i-1, j, m, n)   # Recursive call in upward direction
          flood(i, j+1, m, n)   # Recursive call in right direction
          flood(i, j-1, m, n)   # Recursive call in left direction
          
        oldColor = image[sr][sc]    # We calculate oldColor first using the coordinates (sr , sc)
        if oldColor == color:
          return image
        m, n = len(image), len(image[0])
        flood(sr, sc, m, n)
        return image
      
      
        """
        Time Complexity:  O(N * M)
        Space Complexity: O(N * M)
        """
