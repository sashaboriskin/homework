def shell_sort(a):
  N = len(a)
  K = N // 2
  while K > 0:
    i = K
    while i < N:
      t = a[i]
      j = i
      while j >= K:
        if t < a[j - K]:
          a[j] = a[j - K]
        else:
          break
        j-=K
      a[j] = t
      i+=1
    print(a)
    K = K // 2
  return a  

a = [8, 7, 4, 3, 5, 1]
print(shell_sort(a))
