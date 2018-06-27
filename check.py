def unical(a):
  a = list(a)
  s = []
  for i in range(len(a)):
    if a[i] not in s:
      s.append(a[i])
  return s      #возвращаем уникальный список

def check(key, value):
  a = unical(key)
  b = unical(value)
  a = sorted(a)
  b = sorted(b)
  if a == b:
    print('True')  #два слова совпадают
  else:
    print('False') #два слова не совпадают

a = ['acb', 'accb', 'bac', 'aabc']
for i in a:
  check('abc', i)
