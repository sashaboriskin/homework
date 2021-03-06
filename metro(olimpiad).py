def recurse(A, a, b, n):
  if n == 0:
    for l in range(len(A)):
      if a in A[l] and b in A[l]:
        return True
  else:
    for l in range(len(A)):
      if a in A[l]:
        B = A[:] #deep copy
        B.pop(l) 
        for h in range(len(A[l])): 
          if recurse(B, A[l][h], b, n-1):
            return True
  return False

A = []
N = int(input())
M = int(input())

for k in range(M):       
  string = input()       
  c = string.split(' ')  
  for i in range(len(c)):
    c[i] = int(c[i])     
  c = c[1:]
  
  A.append(c)    

a, b =  (int(val) for val in input().split())

nodes = -1
for i in range(M):
  if recurse(A, a, b, i):
    nodes = i
    break

print(nodes)
