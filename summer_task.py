def sum_array(a):
  summ = 0
  for i in a:
    summ = summ + i
  return summ

n = 12
k = 3

for i in range(n):
  new_spisok = []
  if i != 0:
    new_spisok.append(i)
  for j in range(n):
    if j != i:
      if j != 0:
        new_spisok.append(j)
    else:
      continue
    for l in range(n):
      if l !=j :
        if l != 0:
          new_spisok.append(l)
      else:
        continue
      if sum_array(new_spisok) == 12:
        print(new_spisok)
