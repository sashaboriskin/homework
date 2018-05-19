def fff(a, start, stop):
  if stop == start:
    return
  wall = start
  for i in range(start, stop - 1):
    
    if a[i] < a[stop]:
      a[i], a[wall] = a[wall], a[i]
      wall+=1
  a[stop], a[wall] =  a[wall], a[stop]

  if stop - start == 1:
    return
  fff(a, wall, stop)
  fff(a, start, wall - 1)

a = [3, 5, 1, 8, 7, 4]
fff(a, 0, len(a)-1)
print(a)
