from tkinter import *                                                             
from tkinter import messagebox                                                        
from tkinter import ttk                                                               
import math                                                                           
import sys                                                                            
                                                                                      
window = Tk()                                                                         
window.title("Calculator")                                                        

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
    print(units[new_units])
  elif len(str(n)) == 2:
    if n == 11:
      print(tricks[1])
    elif n == 12:
      print(tricks[2])
    elif n == 13:
      print(tricks[3])
    elif n == 14:
      print(tricks[4])        
    elif n == 15:
      print(tricks[5])        
    elif n == 16:
      print(tricks[6])        
    elif n == 17:
      print(tricks[7])        
    elif n == 18:
      print(tricks[8])
    elif n == 19:
      print(tricks[9])
    else:
      print(dozens[new_dozens], units[new_units])
  elif len(str(n)) == 3:
    b = str(n)
    s = b[1] + b[2]
    if s == 11:
      print(hundreds[new_hundreds], tricks[1])
    elif s == 12:
      print(hundreds[new_hundreds], tricks[2])
    elif s == 13:
      print(hundreds[new_hundreds], tricks[3])        
    elif s == 14:
      print(hundreds[new_hundreds], tricks[4])        
    elif s == 15:
      print(hundreds[new_hundreds], tricks[5])        
    elif s == 16:
      print(hundreds[new_hundreds], tricks[6])        
    elif s == 17:
      print(hundreds[new_hundreds], tricks[7])        
    elif s == 18:
      print(hundreds[new_hundreds], tricks[8])        
    elif s == 19:
      print(hundreds[new_hundreds], tricks[9])        
    else:
      print(hundreds[new_hundreds], dozens[new_dozens], units[new_units])
  elif len(str(n)) == 4:
    v = str()  
    m = v[2] + v[3]        
    if m == 11:
      print(thousands[new_thousands], hundreds[new_hundreds], tricks[1])
    elif m == 12:  
      print(thousands[new_thousands], hundreds[new_hundreds], tricks[2])
    elif m == 13:  
      print(thousands[new_thousands], hundreds[new_hundreds], tricks[3])
    elif m == 14:  
      print(thousands[new_thousands], hundreds[new_hundreds], tricks[4])
    elif m == 15:  
      print(thousands[new_thousands], hundreds[new_hundreds], tricks[5])
    elif m == 16:  
      print(thousands[new_thousands], hundreds[new_hundreds], tricks[6])
    elif m == 17:  
      print(thousands[new_thousands], hundreds[new_hundreds], tricks[7])
    elif m == 18:  
      print(thousands[new_thousands], hundreds[new_hundreds], tricks[8])
    elif m == 19:  
      print(thousands[new_thousands], hundreds[new_hundreds], tricks[9])
    else:
      print(thousands[new_thousands], hundreds[new_hundreds], dozens[new_dozens], units[new_units])                                                                                      
def calculator(key):                                                                  
    global memory                                                                     
    if key == "=":                                                                    
        str1 = "-+0123456789.*/"                                                      
        #исключение                                                                   
        if calc_entry.get()[0] not in str1:                                           
            calc_entry.insert(END, "First symbol is not number!")                     
            messagebox.showerror("Error!", "You did not enter the number!")           
        #ответ                                                                        
        try:                                                                          
            result = eval(calc_entry.get())                                           
            calc_entry.insert(END, "=" + str(result))                                 
        except:                                                                       
            calc_entry.insert(END, "Error!")                                          
            messagebox.showerror("Error!", "Check the correctness of data")           
    elif key == "C":                                                                  
        calc_entry.delete(0, END)                                                     
    elif key == "Exit":                                                               
        window.after(1, window.destroy)                                                    
        sys.exit                                                                      
    elif key == "SASHA":
      calc_entry.insert(END, "(" + string(key) + ")")
        
    else:                                                                             
        if "=" in calc_entry.get():                                                   
            calc_entry.delete(0, END)                                                 
        calc_entry.insert(END, key)                                                   
                                                                                      
                                                                                      
bttn_list = [                                                                         
"7", "8", "9", "+", "*",                                                              
"4", "5", "6", "-", "/",                                                              
"1", "2", "3",  "=", "Exit",                                                          
"0", ".", "C",  "SASHA" ,                                                                     
]                                                                                     
r = 1                                                                                 
c = 0                                                                                 
for i in bttn_list:                                                                   
    rel = ""                                                                          
    cmd=lambda x=i: calculator(x)                                                     
    ttk.Button(window, text=i, command = cmd, width = 10).grid(row=r, column = c)       
    c += 1                                                                            
    if c > 4:                                                                         
        c = 0                                                                         
        r += 1                                                                        
calc_entry = Entry(window, width = 33)                                                   
calc_entry.grid(row=0, column=0, columnspan=5)                                        
                                                                                      
window.mainloop() 
