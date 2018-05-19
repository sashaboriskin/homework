from tkinter import *

def string(n):
    if n == 0:
        print("ноль")
    units = [' ', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    dozens = [' ', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
              'девяносто']
    hundreds = [' ', 'сто', 'двести', 'триста', 'четыресто', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousands = [' ', 'одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи', 'пять тысяч', 'шесть тысяч',
                 'семь тысяч', 'восемь тысяч', 'девять тысяч']
    tricks = [' ', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестьнадцать',
              'семьнадцать', 'восемьнадцать', 'девятьнадцать']
    new_thousands = (n % 10000) // 1000
    new_hundreds = (n % 1000) // 100
    new_dozens = (n % 100) // 10
    new_units = n % 10

    if len(str(n)) == 1:
        print(tricks[new_units])
    elif len(str(n)) == 2:
        print(dozens[new_dozens], units[new_units])
    elif len(str(n)) == 3:
        print(hundreds[new_hundreds], dozens[new_dozens], units[new_units])
    elif len(str(n)) == 4:
        print(thousands[new_thousands], hundreds[new_hundreds], dozens[new_dozens], units[new_units])



window = Tk()

window.title('Jeka')
window.geometry('480x360')
window["bg"] = "white"

entry = Entry(window , width = 100)
entry.grid(row=55, column=55, columnspan=55)

