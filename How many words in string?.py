str = input("Enter the string: ")
str = str.split()
for i in range(len(str)-1):
    if str[i] == '-':
        str.pop(i)
    elif str[i] == '<':
        str.pop(i)
    elif str[i] == '>':
        str.pop(i)
    elif str[i] == '!':
        str.pop(i)
    elif str[i] == '.':
        str.pop(i)
    elif str[i] == ',':
        str.pop(i)
    elif str[i] == ';':
        str.pop(i)
    elif str[i] == '%':
        str.pop(i)      
    elif str[i] == ':':
        str.pop(i)
    elif str[i] == '?':
        str.pop(i)
    elif str[i] == '*':
        str.pop(i)
    elif str[i] == '(':
        str.pop(i)
    elif str[i] == ')':
        str.pop(i)
    elif str[i] == '+':
        str.pop(i)
    elif str[i] == '/':
        str.pop(i)


print(len(str), 'words')
