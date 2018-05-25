'''
a = [l, b]
b = [9, 13]
'''

def constants(a, b):
    for i in range(len(a)):
        print('int', a[i], '=', b[i], ';')

def void_setup(a, c):
    print('void setup() {')
    for i in range(len(a)):
        if c[i] == 0:
            print('pinMode(', a[i], ',', 'OUTPUT)')
        else:
            print('pinMode(', a[i], ',', 'INPUT)')
    print('}')

def void_loop(a, low_high, an_dig):
    print('void loop() {')
    for i in range(len(a)):
        if an_dig == 0: # 0 = analog
            if low_high == 0: # 0 = low
                print('analogWrite(', a[i], ',', 'LOW);')
                print('delay(500);')
            else:
                print('analogWrite(', a[i], ',', 'HIGH);')
                print('delay(500);')
        else:
            if low_high == 0: # 0 = low
                print('digitalWrite(', a[i], ',', 'LOW);')
                print('delay(500);')
            else:
                print('digitalWrite(', a[i],',' , 'HIGH)')
                print('delay(500);')
    print('}')


a = input('Enter the a: ').split()
b = input('Enter the b: ').split()
c = input('Enter the c(OUTPUT = 0 or INPUT = 1): ').split()
low_high = input('low or high(LOW = 0 or HIGH = 1): ').split()
an_dig = input('analog or digital: ').split()

print('\n')
constants(a, b)
void_setup(a, c)
void_loop(a, low_high, an_dig)
