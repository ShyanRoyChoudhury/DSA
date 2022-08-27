def fib(self,n):
  if n==0:
    return 0
  if n==1 or n==2:
    return 1
  
  ans1=fib(n-1)   //recursion that will give us n-1 value
  ans2=fib(n-2)   //recursion that will give us n-2 value
  
  return ans1 + ans2
  
  """
  
  
  """
