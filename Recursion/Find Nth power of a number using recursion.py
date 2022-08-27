def myPow(self, x, n):
  """
  x: float
  n: int
  """
  if n==0
  return 1

  if n<0:
    x=1/x
    n=abs(n)
    
  temp = self.myPow(x, n//2)
  
  if n%2=0:
    return temp*temp
  else:
    return x*temp*temp
  
  """
  
  """
