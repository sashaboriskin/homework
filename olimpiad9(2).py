def ins_sort(a):
    for i in range(1,len(a)):    
        j = i                    
        d = a[j]              
        while j > 0 and d < a[j-1]: 
            a[j] = a[j-1] 
            j=j-1 
        a[j] = d
    return a

A = int(input())
B = int(input())
C = int(input())

a = [A, B, C]
b = ins_sort(a)
print(a[1])
