n = int(input())
word  = input()
if n != len(word):
    print("Error")
    exit()
k = int(input())

sortw = sorted(set(word))
print(sortw)

if k>n:
    a = k - n
    for i in range(a):
        new_word = word + min(sortw)
    print(new_word)
else:
    for i in range(len(word)):
        if word[-i] == max(sortw):
            word.pop(-i)
            t+=1
        else:
           word[-i] = sortw(-i + 1) #'list' object is not callable
    for i in range(t):
        new_word = word + min(sortw)
    print(new_word)
    
