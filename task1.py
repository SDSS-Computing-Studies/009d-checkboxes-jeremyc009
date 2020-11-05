#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk 
from tkinter import *


def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal
    num=0
    for i in range(0,8):
        
        val=binary[i]
        if val==1:
            value=128/(2**i)
            num=num+value
            
        elif val==0:
            pass
    return num


    return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    num=decimal
    binary=[]
    for i in range(0,8):
        nextVal=128/(2**i)
        res=num-nextVal
        
        if res>=0:
            binary.insert(i,1)
            num=res
        elif res<0:
            binary.insert(i,0)
            num=res+nextVal
        
        
    binary = tuple(binary)
    return binary


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal=dec.get()
    
    binary = decimal_to_binary(decimal)
    
    for i in range(0,8):
        st[i].set(binary[-(i+1)])

def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary=[]
    for i in range(0,8):
        
        binary.insert(i,st[-(i+1)].get())

    decimal = binary_to_decimal(binary)
    dec.set(decimal)



win = tk.Tk()

l1=tk.Label(win,text='Binary/Decimal Converter!')
dec=IntVar()
entry=tk.Entry(win,textvariable=dec)
b1 = tk.Button(win, text="Convert to Binary", command=get_binary)
b2 = tk.Button(win, text="Convert to Decimal", command=get_decimal)
st=[]
cb=[]
for i in range(0,8):
    s1=IntVar()
    st.insert(i,s1)
    s1.set(0)
for i in range(0,8):
    li='cb'+str(i)
    cb.insert(i,li)

for i in range(0,8):
    cb[i]=tk.Checkbutton(win,variable=st[i])

for i in range(0,8):
    cb[8-(i+1)].grid(row=2,column=(i+1))
l1.grid(row=1,column=1,columnspan=8)
b1.grid(row=3,column=1,columnspan=4)
b2.grid(row=3,column=5,columnspan=4)
entry.grid(row=4,column=1,columnspan=8)
win.mainloop()