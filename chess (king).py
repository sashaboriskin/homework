import sys

while True:
    print("Press Gor1 and Ver1 fo first point:")
    Gor1 = int(input())
    Ver1 = int(input())

    print("Press Gor2 and Ver2 for second point:")
    Gor2 = int(input())
    Ver2 = int(input())

    deltaGor =  Gor1 - Gor2

    deltaVer =  Ver1 - Ver2

    if ( deltaGor == 1 ) or  (deltaGor == -1) :
        if (deltaVer == 0) or (deltaVer == 1) or (deltaVer == -1):
            print("Yes")
        else:
            print("No")
    elif ( deltaVer == 1 ) or  (deltaVer == -1) :
        if (deltaVer == 0) or (deltaVer == 1) or (deltaVer == -1):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

    print("Press x to exit, otherwise continue")
    exitcode = input()
    if(exitcode == 'x') :
       sys.exit()

