from tkinter import *
def one():
    print(1)
def two():
    print(2)
def three():
    print(3)
def four():
    print(4)
def five():
    print(5)
def six():
    print(6)
def seven():
    print(7)
def eight():
    print(8)
def nine():
    print(9)
def non():
    print(0)
root = Tk()
button1 = Button(root, bg='grey', text='1', command = one)
button1.pack()
button2 = Button(root, bg='grey', text='2', command = two)
button2.pack()
button3 = Button(root, bg='grey', text='3', command = three)
button3.pack()
button4 = Button(root, bg='grey', text='4', command = four)
button4.pack()
button5 = Button(root, bg='grey', text='5', command = five)
button5.pack()
button6 = Button(root, bg='grey', text='6', command = six)
button6.pack()
button7 = Button(root, bg='grey', text='7', command = seven)
button7.pack()
button8 = Button(root, bg='grey', text='8', command = eight)
button8.pack()
button9 = Button(root, bg='grey', text='9', command = nine)
button9.pack()
button0 = Button(root, bg='grey', text='0', command = non)
button0.pack()
root.mainloop()



