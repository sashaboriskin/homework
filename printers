
import math
n = int(input())
x = int(input())
y = int(input())

n = n-1
tstart = 1/max(x,y)

t = n/(x+y)#minimal possible time 
kx = math.ceil(x*t)#number of pages for printer1
ky = math.ceil(y*t)#number of pages for printer2
tx = kx/x#time for printing kx pages on printer 1 
ty = ky/y#time for printing ky pages on printer 2
tmin = min(tx,ty) + tstart
print(tmin)
