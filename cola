import math
A = int(input()) # 50
B = int(input()) # 70 
min_50 = (A-1)*50
max_50 = A*50
min_70 = (B-1)*70
max_70 = B*70
 
'''min_50 < x <= max_50
min_70 < x <= max_70
min_70 < y <= max_50'''

min_60 = max(min_50, min_70)
max_60 = min(max_50, max_70)

if min_60 < max_60:
    if math.ceil(min_60/60) == math.ceil(max_60/60):
        print(math.ceil(max_60/60))
    else:
        print(math.ceil(min_60/60), math.ceil(max_60/60))
else:
    print("-1")
