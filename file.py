f = open('sasha.txt', 'r')

parties=[]
for i in range(7):
    parties.append(0)

for str in f:
    num = str.count("+")
    if num != 1:
        continue
    idx = str.index("+")
    parties[idx]+=1

print(parties)    

