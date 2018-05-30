import from functions *


def constants(a, b):
    #a - peremenaya
    #b - znachenie
    for i in range(len(a)):
        print('int', a[i], '=', b[i], ';')


def void_setup(a, y):
    #a - list of pins  //   a = [8, 9, 13]
    #y - list of znachiniya   //  b = [OUTPUT, INPUT, INPUT]
    print('void setup() {')
    for i in range(len(a)):
        pinMode(a[i], y[i])
    print('}')


def void_loop(a, l, z):
    #a - list of pins  //  a = [8, 9, 13]
    #l - list of znacheniya  //  b = [LOW, HIGH, HIGH]
    #z - list of tipes pins  //  c = [analog, digital, digital]
    print('void loop() {')
    for i in range(len(a)):
        if z[i] == 'analog':
            analogWrite(a[i], l[i])
            delay(500)
        else:
            digitalWrite(a[i], l[i])
            delay(500)
    print('}')


a = input('Enter the a: ').split()
b = input('Enter the b: ').split()
c = input('Enter the c(OUTPUT = 0 or INPUT = 1): ').split()
low_high = input('low or high(LOW = 0 or HIGH = 1): ').split()
an_dig = input('analog or digital: ').split()

print('\n')
constants(a, b)
void_setup(a, b)
void_loop(a, b, c)
