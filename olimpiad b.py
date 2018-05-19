a = [] 
q = 0
for i in range(int(input("Enter the number: "))): 
    a.append(int(input("Enter the new element: ")) ) 

for j in range(len(a)): 
    s = a[j] 
    q = 2*s 
    for k in range(j+1, len(a)) :
        q = q + a[k]
        if a[j] == a[k]:
          sum = max(sum, q)


print(sum)
