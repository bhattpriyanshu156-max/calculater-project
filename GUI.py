from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=20, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def click(n):
    e.insert(END, n)

def clear():
    e.delete(0, END)

def equal():
    result = eval(e.get())
    e.delete(0, END)
    e.insert(END, result)

Button(root, text='1', command=lambda: click(1)).grid(row=1, column=0)
Button(root, text='2', command=lambda: click(2)).grid(row=1, column=1)
Button(root, text='3', command=lambda: click(3)).grid(row=1, column=2)
Button(root, text='+', command=lambda: click('+')).grid(row=1, column=3)

Button(root, text='4', command=lambda: click(4)).grid(row=2, column=0)
Button(root, text='5', command=lambda: click(5)).grid(row=2, column=1)
Button(root, text='6', command=lambda: click(6)).grid(row=2, column=2)
Button(root, text='-', command=lambda: click('-')).grid(row=2, column=3)

Button(root, text='7', command=lambda: click(7)).grid(row=3, column=0)
Button(root, text='8', command=lambda: click(8)).grid(row=3, column=1)
Button(root, text='9', command=lambda: click(9)).grid(row=3, column=2)
Button(root, text='*', command=lambda: click('*')).grid(row=3, column=3)

Button(root, text='0', command=lambda: click(0)).grid(row=4, column=0)
Button(root, text='C', command=clear).grid(row=4, column=1)
Button(root, text='=', command=equal).grid(row=4, column=2)
Button(root, text='/', command=lambda: click('/')).grid(row=4, column=3)

root.mainloop()
