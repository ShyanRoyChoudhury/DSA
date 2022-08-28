def isPalindrome(self, s):
  
  def isPalindromehelper(l,r,str):
    
    if l>=r:
      return True            //returns True when left pointer length is equal or more than the right pointer length, i.e. palindrome. 
    
    if str[l]!=str[r]:      //returns False when left pointer character is not equal to right pointer character.
      return False
    return isPalindromehelper(l+1,r-1,str)
  
  newString = ""
  
  for char in s:
    if char.isalnum() == False:
      continue
    if char == " ":
      continue
    if char.isupper():
      char = char.lower()
    
    newString += char
    
  return isPalindromehelper(0,len(newString)-1,newString)

"""
T.C: O(n)
S.C: O(n)
"""
