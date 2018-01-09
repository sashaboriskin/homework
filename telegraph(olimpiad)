X = input()
Z = input()

#1 We delete the beginning of the sequence Z that can be obtained with X
doubleX = X + X
for i in range(len(doubleX)):
  startStr = doubleX[i:]
  if Z.find( startStr ):
    continue #
  Z = Z[len(startStr):]
  break

#2 We delete the repeated subsequences X
while True:
  if Z.find(X):
    break
  Z = Z[len(X):]

print(Z) 
