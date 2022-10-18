# A simple Calculator

from tkinter import *
from math import sqrt

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_add():
    global f_num
    global math
    first_number = e.get()
    math = 'Addition'
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    global f_num
    global math
    first_number = e.get()
    math = 'Subtraction'
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    global f_num
    global math
    first_number = e.get()
    math = 'Division'
    f_num = int(first_number)
    e.delete(0, END)


def button_sqrt():
    first_number = e.get()
    f_number = int(first_number)
    e.delete(0, END)
    sqrt_n = sqrt(f_number)
    if int(sqrt_n) ** 2 == f_number:
        e.insert(0, int(sqrt_n))
    else:
        e.insert(0, sqrt_n)


def button_multiply():
    global f_num
    global math
    first_number = e.get()
    math = 'Multiplication'
    f_num = int(first_number)
    e.delete(0, END)


def button_clear():
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'Addition':
        e.insert(0, f_num + int(second_number))
    if math == 'Subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'Multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'Division':
        div_n = f_num / int(second_number)
        if int(div_n) * int(second_number) == f_num:
            e.insert(0, int(div_n))
        else:
            e.insert(0, div_n)


button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_square_root = Button(root, text='SQRT', padx=30, pady=20, command=button_sqrt)
button_divide = Button(root, text='/', padx=71, pady=20, command=button_divide)
button_multiply = Button(root, text='*', padx=40, pady=20, command=button_multiply)
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_clear = Button(root, text='Clear', padx=60, pady=20, command=button_clear)
button_equal = Button(root, text='=', padx=70, pady=20, command=button_equal)
button_sub = Button(root, text='-', padx=40, pady=52, command=button_sub)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_square_root.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_multiply.grid(row=6, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1)
button_clear.grid(row=4, column=1)
button_sub.grid(row=4, column=2, rowspan=2)

root.mainloop()
