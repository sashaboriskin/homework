def ins_sort(a):
    for i in range(1,len(a)):    
        j = i                    
        d = a[j]              
        while j > 0 and d < a[j-1]: 
            a[j] = a[j-1] 
            j=j-1 
        a[j] = d
    return a

a = [8, 7, 4, 3, 5, 1]
print(ins_sort(a))
