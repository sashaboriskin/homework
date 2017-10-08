import sys
while True:

    print("Enter the number:")
    number = int(input())
    previus2 = 0
    previus = 1
    number_fibonachi = previus

    if number == 1:
        print("number_fibonachi = 0")
    else:
        for i in range(2, number):
            number_fibonachi = previus + previus2;
            previus2 = previus   
            previus = number_fibonachi
   

        print("number_fibonachi = ", number_fibonachi)


    print("Press x to exit, otherwise continue")
    exitcode = input()
    if(exitcode == 'x') :
       sys.exit()
   
