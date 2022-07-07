def solution(x,y):
  
  x = set(x)
  y = set(y)
  
  s = list(x ^ y)
  
  return s[0]
  
