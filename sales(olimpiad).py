import math

N = int(input())
price = input()
price = price.split(" ")
for i in range(len(price)):
    price[i] = int(price[i])

if N is not len(price):
    print("-1")
    exit()

minPrice = 9999999999999999999
for i in range(int(math.pow(2, N))):
    firstMonthWaste = 0
    secondMonthWaste = 0
    coupons = 0
    for j in range(N):
        if i & (1 << j):
            firstMonthWaste += price[j];
            coupons += int(price[j] / 1000)
        else:
            secondMonthWaste += price[j];

    maxSale = coupons * 500
    if secondMonthWaste * 0.2 < maxSale:
        maxSale = secondMonthWaste * 0.2

    curPrice = firstMonthWaste + secondMonthWaste - maxSale
    minPrice = min(minPrice, curPrice)


print('{0:.2f}'.format(minPrice))
