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
st1=IntVar()
st1.set(0)
b1 = tk.Button(win, text="Convert to Binary", command=get_binary)
b2 = tk.Button(win, text="Convert to Decimal", command=get_decimal)
st1=IntVar()
st1.set(0)
st2=IntVar()
st2.set(0)
st3=IntVar()
st3.set(0)
st4=IntVar()
st4.set(0)
st5=IntVar()
st5.set(0)
st6=IntVar()
st6.set(0)
st7=IntVar()
st7.set(0)
st8=IntVar()
st8.set(0)
st=[st1,st2,st3,st4,st5,st6,st7,st8]
cb1 = tk.Checkbutton(win,variable=st[0])
cb2 = tk.Checkbutton(win,variable=st[1])
cb3 = tk.Checkbutton(win,variable=st[2])
cb4 = tk.Checkbutton(win,variable=st[3])
cb5 = tk.Checkbutton(win,variable=st[4])
cb6 = tk.Checkbutton(win,variable=st[5])
cb7 = tk.Checkbutton(win,variable=st[6])
cb8 = tk.Checkbutton(win,variable=st[7])
l1.grid(row=1,column=1,columnspan=8)
cb8.grid(row=2,column=1)
cb7.grid(row=2,column=2)
cb6.grid(row=2,column=3)
cb5.grid(row=2,column=4)
cb4.grid(row=2,column=5)
cb3.grid(row=2,column=6)
cb2.grid(row=2,column=7)
cb1.grid(row=2,column=8)
b1.grid(row=3,column=1,columnspan=4)
b2.grid(row=3,column=5,columnspan=4)
entry.grid(row=4,column=1,columnspan=8)
win.mainloop()