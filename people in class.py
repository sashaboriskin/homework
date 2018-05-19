a = int(input("Enter the people of first class:"))
b = int(input("Enter the people of second class:"))
c = int(input("Enter the people of third class:"))

if a%2 != 0:
    parta_a = (a//2) + 1
else:
    parta_a = a/2


if b%2 != 0:
    parta_b = (b//2) + 1
else:
    parta_b = b/2


if c%2 != 0:
    parta_c = (c//2) + 1
else:
    parta_c = c/2


N = parta_a + parta_b + parta_c
print(N)
