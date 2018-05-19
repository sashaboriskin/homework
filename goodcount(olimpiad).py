a = []
n = int(input("Enter the N: "))
for d in range(n):
  a.append(int(input("Enter the new element: ")))

countgood = 0
max_volua = max(a)
for i in range(max_volua):
  for j in range(n-1):
    if a[j] == 0:
      continue
    a[j]-=1
    if a[j+1] != 0:   
      countgood+=1


print(countgood )
