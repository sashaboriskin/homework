def binary_system(n):
    b = 2147483648;
    str = ''
    while b > 0:
        z = n & b;
        if z == 0:
            str = str + '0'
        else:
            str = str + '1'
        b = b >> 1;
    return str
n = int(input("Enter the number: "))
print(binary_system(n))
