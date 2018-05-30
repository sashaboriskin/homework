def pinMode(a, b):
    # a - pin
    # b - INPUT or OUTPUT
    print('pinMode(', a, ',', b, ')', ';')


def digitalWrite(a, b):
    # a - pin
    # b - HIGH OR LOW
    print('digitalWrite(', a, ',', b, ')', ';')


def digitalRead(a):
    # a - pin
    print('digitalRead(', a, ')', ';')


def analogRead(a):
    # a - pin
    print('analogRead(', a, ')', ';')


def analogWrite(a, b):
    # a - pin
    # b - b(int)(0-1023)
    print('analogWrite(', a, ',', b, ')', ';')


def delay(time):
    # time - time
    print('delay(', time, ')', ';')


def IF(a, z, c):
    # a - peremenaya
    # z - znak
    # c - peremenaya or number
    print('if(', a, z, c, ')', '{')


def ElSE():
    print('else', '{')


def FOR(start, stop, step):
    print('for(', start, ';', stop, ';', step, ')', '{')


def WHILE(a, z, c):
    print('while(', a, z, c, ')', '{')
