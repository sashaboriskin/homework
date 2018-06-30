n = 8
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [7, 4, 2, 8, 6, 1, 3, 5]

vibor = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j]:
            vibor = False
 
if vibor == True:
    print('NO')
else:
    print('YES')


'''

1 7      
2 4
3 2
4 8
5 6
6 1
7 3
8 5

'''
