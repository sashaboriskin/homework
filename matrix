a = input('Enter the first equation: ')
b = input('Enter the second equation: ')
a = a.split()
b = b.split()
for i in range(len(a)):
	a[i] = int(a[i])
	b[i] = int(b[i])
print(a)
print(b)
c = a[0]/b[0]
for i in range(len(a)):
	b[i]=-(b[i]*c)
print(b)
for i in range(len(a)):
	a[i]=a[i]+b[i]
print(a)
c = -(b[1]/a[1])
for i in range(len(a)):
	a[i] = a[i]*c
print(a)
for i in range(len(a)):
	b[i]=b[i]+a[i]
print(b)
print('x = ', b[2]/b[0])
print('y = ', a[2]/a[1])
input('Enter the x, if you want exit from programm: ')
