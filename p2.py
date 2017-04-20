def combination(n, r):
  residual = []
  residual.append((n, r))
  result = 0

  while len(residual):
    n, r = residual.pop()
    if r == 0:
      result = result + 1
    elif n<r:
      pass
    else:
      residual.append((n-1, r))
      residual.append((n-1, r-1))

  return result    
print (combination(5,2))