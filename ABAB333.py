def function(s):
  for i in s:
    if s[i]=='A':
      s[i]='AB'
  for i in s:
    if (s[i]=='B') and (s[i+1]=='B'):
      s[i]=''
      s[i+1]='C'
  return s 

s = 'ABAB'
a=0
b=0
c=0

for i in range(333):
  s = function(s)

for i in range(len(s)):
  if s[i]=='A':
    a+=1
  elif s[i]=='B':
    b+=1
  else:
    c+=1

print(a, b, c)
