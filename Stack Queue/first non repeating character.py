""" Approach : Using Hashmap,
We will traverse the whole array and keep a count of the frequency of each element. If the frequency is one, 
then we return that element. If the occurrence of all the elements is more than one, 
then we simply return the first character of the string.

 

The steps are as follows:

1.We initialize a hash map ‘map’ to store the frequency of each element.

2.We will iterate over the length of the string ‘str’, i.e., i = 0 to i = N - 1:
    We will store the frequency of a character at position i in ‘map’.
    
    If the element already exists in ‘map’, then increment ‘map’ for that character.

3. We will iterate over the length of the string, i.e., i = 0 to i = N - 1:
    If map[str[i]] is 1 then we return the value of str[i] as the final answer.

4. We will return the first character of the string as the final answer.
"""
from collections import *

def firstNonRepeatingCharacter(str):
    
    map = OrderedDict()
    for i in range(len(str)):
        ch = str[i]
        num = map.get(ch, 0)
        map[ch] = num + 1
    
    for i in range(len(str)):
        ch = str[i]
        if map[ch] == 1:
            return ch
        
    return str[0]
  
  
  """
  T.C: O(N), where ‘N’ is the length of the string.
  As we check for all values from1 to ‘N’, there are at most ‘N’ iterations. Hence the overall complexity is O(N). 
  
  S.C: O(N), where ‘N’ is the length of the string.
  We are using a map to count the frequency of each element. Hence, the overall space complexity is O(N).
  """
