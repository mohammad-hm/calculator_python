from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)
root.geometry('400x350')
lable = Label(root, text='Enter : ')
lable.place(x=10, y=20)

entry1 = Entry(root)
entry1.place(x=80, y=20)


def input_Nums():
    print(f"Entered number is : {entry1.get()}")

btn = Button(root, text="+", command=lambda: input_Nums())
btn.place(x=50, y=50)
# btn_2 = Button(root, text="-")
# btn.place(x=20, y=80)

root.mainloop()
