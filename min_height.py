def max_in_array(a):
  maxi = a[0]
  for i in range(len(a)):
    if a[i] > maxi:
      maxi = a[i]
  return maxi

def sum_array(a):
  summ = 0
  for i in a:
    summ = summ + i
  return summ

a = [1, 3, 4, 2, 5]
first = []
second = []
max = max_in_array(a)
first.append(max)
a.remove(max)

for i in range(len(a)):
  sum1 = sum(first)
  sum2 = sum(second)
  if a[i] < sum2:
    first.append(a[i])
  else:
    second.append(a[i])

print(first)
print(second)
