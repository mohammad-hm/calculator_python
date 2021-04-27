from tkinter import *

root = Tk()
root.title("Calculator")
operator = ""
inputNum = StringVar()

root.geometry('300x400')
# root.maxsize(400, 500)
# root.minsize(200, 300)

# lable = Label(root, text='Enter : ')
# lable.place(x=10, y=70)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)
# Grid.columnconfigure(root, 4, weight=1)
# # Grid.rowconfigure(root, 4, weight=1)

display = Entry(root, textvariable=inputNum, insertwidth=3, bg='white', justify='left').grid(row=0, column=0, rowspan=1,
                                                                                             columnspan=4,
                                                                                             sticky="NSWE")

# def input_Nums():
#     print(f"Entered number is : {display.get()}")


btn7 = Button(root, text="7", fg='red', font=("arial", 15, "bold")).grid(row=1, column=0, sticky="NSEW")
btn8 = Button(root, text="8", fg='red', font=("arial", 15, "bold")).grid(row=1, column=1, sticky="NSEW")
btn9 = Button(root, text="9", fg='red', font=("arial", 15, "bold")).grid(row=1, column=2, sticky="NSEW")
add =  Button(root, text="+", fg='red', font=("arial", 15, "bold")).grid(row=1, column=3, sticky="NSEW")
btn4 = Button(root, text="4", fg='red', font=("arial", 15, "bold")).grid(row=2, column=0, sticky="NSEW")
btn5 = Button(root, text="5", fg='red', font=("arial", 15, "bold")).grid(row=2, column=1, sticky="NSEW")
btn6 = Button(root, text="6", fg='red', font=("arial", 15, "bold")).grid(row=2, column=2, sticky="NSEW")
sub =  Button(root, text="-", fg='red', font=("arial", 15, "bold")).grid(row=2, column=3, sticky="NSEW")
btn1 = Button(root, text="1", fg='red', font=("arial", 15, "bold")).grid(row=3, column=0, sticky="NSEW")
btn2 = Button(root, text="2", fg='red', font=("arial", 15, "bold")).grid(row=3, column=1, sticky="NSEW")
btn3 = Button(root, text="3", fg='red', font=("arial", 15, "bold")).grid(row=3, column=2, sticky="NSEW")
multiply = Button(root, text="*", fg='red', font=("arial", 15, "bold")).grid(row=3, column=3, sticky="NSEW")
cls = Button(root, text="C", fg='red', font=("arial", 15, "bold")).grid(row=4, column=0, sticky="NSEW")
btn0 = Button(root, text="0", fg='red', font=("arial", 15, "bold")).grid(row=4, column=1, sticky="NSEW")
equal = Button(root, text="=", fg='red', font=("arial", 15, "bold")).grid(row=4, column=2, sticky="NSEW")
division = Button(root, text="/", fg='red', sfont=("arial", 15, "bold")).grid(row=4, column=3, sticky="NSEW")

# btn7 = Button(cal, c, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
#               text='7').grid(row=1, column=0)
# btn_2 = Button(root, text="-")
# btn.place(x=20, y=80)

root.mainloop()
