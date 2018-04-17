from tkinter import *                                                                 
from tkinter import messagebox                                                        
from tkinter import ttk                                                               
import math                                                                           
import sys                                                                            
                                                                                      
window = Tk()                                                                         
window.title("Calculator")                                                            
                                                                                      
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
        root.after(1,root.destroy)                                                    
        sys.exit                                                                      
    else:                                                                             
        if "=" in calc_entry.get():                                                   
            calc_entry.delete(0, END)                                                 
        calc_entry.insert(END, key)                                                   
                                                                                      
                                                                                      
bttn_list = [                                                                         
"7", "8", "9", "+", "*",                                                              
"4", "5", "6", "-", "/",                                                              
"1", "2", "3",  "=", "Exit",                                                          
"0", ".", "C",                                                                        
]                                                                                     
r = 1                                                                                 
c = 0                                                                                 
for i in bttn_list:                                                                   
    rel = ""                                                                          
    cmd=lambda x=i: calculator(x)                                                     
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)       
    c += 1                                                                            
    if c > 4:                                                                         
        c = 0                                                                         
        r += 1                                                                        
calc_entry = Entry(root, width = 33)                                                  
calc_entry.grid(row=0, column=0, columnspan=5)                                        
                                                                                      
root.mainloop()                                                                       
