print("7t + 3n + 10y = N")
print("Enter N")
user_var = int(input())
t = -101
n = -101
y = -101
summa = 0
while (t < 100):
    t+=1
    n = -100
    while (n < 100):
        n+=1
        y = -100
        while (y < 100):
            y+=1
            summa = 7*t + 3*n + 10*y
            if summa == user_var:
                print("t =", t, "n = ", n, "y =", y)
                break 

print("press any key...")
user_var = int(input())
                            

