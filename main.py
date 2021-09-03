# Simple CalculatorV3

from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input .set(operator)

def AC():
    global operator
    operator=""
    text_Input.set("")

def Equals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

calc = Tk()
calc.title("Simple CalculatorV3")
calc.iconbitmap("icon.ico")
calc.minsize(360, 380)
calc.maxsize(360, 380)
operator=""

text_Input = StringVar()

txtbox = Entry(calc, font=("arial", 14), textvariable=text_Input, bd=70, insertwidth=8,
               bg="grey", justify="right").grid(columnspan=4)
### Buttons 1-9 on clalculaotor
btn1 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
              text="1", command=lambda:btnClick(1)).grid(row=1, column=0)

btn2 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
              text="2", command=lambda:btnClick(2)).grid(row=1, column=1)

btn3 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
              text="3", command=lambda:btnClick(3)).grid(row=1, column=2)

btn4 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
              text="4", command=lambda:btnClick(4)).grid(row=2, column=0)

btn5 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
              text="5", command=lambda:btnClick(5)).grid(row=2, column=1)

btn6 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
              text="6", command=lambda:btnClick(6)).grid(row=2, column=2)

btn7 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
              text="7", command=lambda:btnClick(7)).grid(row=3, column=0)

btn8 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
              text="8", command=lambda:btnClick(8)).grid(row=3, column=1)

btn9 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
              text="9", command=lambda:btnClick(9)).grid(row=3, column=2)

btn0 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
              text="0", command=lambda:btnClick(0)).grid(row=4, column=1)
### Buttons +, -, *, /, AC, = ###

Addition = Button(calc, padx=13, bd=8, fg="black", font=("arial", 14),
                  text="+", command=lambda:btnClick("+")).grid(row=1, column=3)

subtraction = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
                     text="-", command=lambda:btnClick("-")).grid(row=2, column=3)

multiplication = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
                        text="*", command=lambda:btnClick("*")).grid(row=3, column=3)

division = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
                  text="/", command=lambda:btnClick("/")).grid(row=4, column=3)

Equals = Button(calc, padx=16, bd=8, fg="black", font=("arial", 14),
                text="=", command = Equals).grid(row=4, column=2)

AC = Button(calc, padx=8, bd=8, fg="black", font=("arial", 14),
                text="AC", command = AC).grid(row=4, column=0)

calc.mainloop()
