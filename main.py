import tkinter
from tkinter import *
import re

root = Tk()
root.title("Calculator")
operator = ""


def callback(input_num):
    if input_num.isdigit():
        print(input_num)
        return True

    elif input_num == "":
        print(input_num)
        return True

    else:
        print(input_num)
        return False


root.geometry('300x400')
root.minsize(200, 300)
root.maxsize(400, 500)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)

reg = root.register(callback)
display = Entry(root, insertwidth=3, bg='white', justify='left')
display.grid(row=0, column=0, rowspan=1, columnspan=4, sticky="NSWE")
display.config(validate="key", validatecommand=(reg, '%P'))


btn7 = Button(root, text="7", fg='red', font=("arial", 15, "bold")).grid(row=1, column=0, sticky="NSEW")
btn8 = Button(root, text="8", fg='red', font=("arial", 15, "bold")).grid(row=1, column=1, sticky="NSEW")
btn9 = Button(root, text="9", fg='red', font=("arial", 15, "bold")).grid(row=1, column=2, sticky="NSEW")
add = Button(root, text="+", fg='red', font=("arial", 15, "bold")).grid(row=1, column=3, sticky="NSEW")
btn4 = Button(root, text="4", fg='red', font=("arial", 15, "bold")).grid(row=2, column=0, sticky="NSEW")
btn5 = Button(root, text="5", fg='red', font=("arial", 15, "bold")).grid(row=2, column=1, sticky="NSEW")
btn6 = Button(root, text="6", fg='red', font=("arial", 15, "bold")).grid(row=2, column=2, sticky="NSEW")
sub = Button(root, text="-", fg='red', font=("arial", 15, "bold")).grid(row=2, column=3, sticky="NSEW")
btn1 = Button(root, text="1", fg='red', font=("arial", 15, "bold")).grid(row=3, column=0, sticky="NSEW")
btn2 = Button(root, text="2", fg='red', font=("arial", 15, "bold")).grid(row=3, column=1, sticky="NSEW")
btn3 = Button(root, text="3", fg='red', font=("arial", 15, "bold")).grid(row=3, column=2, sticky="NSEW")
multiply = Button(root, text="*", fg='red', font=("arial", 15, "bold")).grid(row=3, column=3, sticky="NSEW")
cls = Button(root, text="C", fg='red', font=("arial", 15, "bold")).grid(row=4, column=0, sticky="NSEW")
btn0 = Button(root, text="0", fg='red', font=("arial", 15, "bold")).grid(row=4, column=1, sticky="NSEW")
equal = Button(root, text="=", fg='red', font=("arial", 15, "bold")).grid(row=4, column=2, sticky="NSEW")
division = Button(root, text="/", fg='red', font=("arial", 15, "bold")).grid(row=4, column=3, sticky="NSEW")


root.mainloop()
