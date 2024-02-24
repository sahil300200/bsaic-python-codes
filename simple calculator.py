# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:05:35 2023

@author: admin
"""

# simple calclulator

print("1 for sun,2 for subtract ,3 for multiplication,4 for division")

a = eval(input("enter a number:"))
b = eval(input("enter a numbe:"))
ch = int(input("enter a choice:"))

if ch==1:
    c = a + b 
    print("sum:",c)
    
elif ch==2:
    c = a - b
    print("subtract:",c)

elif ch==3:
    c = a * b 
    print("multplication:",c)
    
elif ch==4:
    c = a / b
    print("division:",c)
    
else:
    print(" error you enter a wrong input you such an idiot")
    
    
