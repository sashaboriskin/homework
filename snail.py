def snail(snail_map):
  n = len(snail_map)
  nums = []
  a = 0
  b = n-1
  c = 0
  d = n-1

  while a>b:
    for j in range(a, b):
      nums.append(snail_map[c][j])
    for i in range(c, d):
      nums.append(snail_map[i][b])
    for j in range(d, a, -1):
      nums.append(snail_map[d][j])
    for i in range(d, a, -1):
      nums.append(snail_map[i][a])
    a+=1
    b-=1
    c+=1
    d-=1
    if ()
