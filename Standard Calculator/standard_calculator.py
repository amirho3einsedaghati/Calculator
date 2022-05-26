from tkinter import *
from tkinter import messagebox

# ================================= settings =====================================

my_calc = Tk()
my_calc.title("Standard Calculator")
my_calc.geometry("322x470")
my_calc.resizable(width=False, height=False)
backgroundColor_GUI = ("gray", "white","powder blue")
my_calc.configure(bg=backgroundColor_GUI[0])

# ================================= Variables =====================================

numAndOp = ""
value_res = StringVar()

# ============================= Frames =================================

btn_frame = Frame(my_calc, width=320, height=300, bg=backgroundColor_GUI[0])
btn_frame.pack(side=BOTTOM)

res_frame = Frame(my_calc, width=320, height=170)
btn_frame.pack(side=BOTTOM)


# ================================= Functions =====================================

def showBtnClick(operatorAndoperand):
    global numAndOp
    numAndOp += str(operatorAndoperand)
    value_res.set(numAndOp)


def btnClear():
    global numAndOp
    value_res.set("")
    numAndOp = ""


def equalsBtn():
    global numAndOp

    try:
        res = str(eval(numAndOp))
        value_res.set(res)
        numAndOp = ""

    except ZeroDivisionError:
        messagebox.showerror("ZeroDivisionError", "you can't divide a number by zero")

    except SyntaxError:
        btnClear()


# ============================= Buttons =================================

div_btn = Button(btn_frame, text="/", padx=24, pady=2, fg="black",font=("arial", 20, "bold"),bd=3,
                 highlightbackground=backgroundColor_GUI[0],
                 bg=backgroundColor_GUI[2], command=lambda: showBtnClick("/"))
div_btn.place(x=240, y=58)

mul_btn = Button(btn_frame, text="*", padx=22, pady=2, fg="black",font=("arial", 20, "bold"),bd=3,
                 highlightbackground=backgroundColor_GUI[0],
                 bg=backgroundColor_GUI[2], command=lambda: showBtnClick("*"))
mul_btn.place(x=241, y=118)

minus_btn = Button(btn_frame, text="-", padx=23, pady=2, fg="black",font=("arial", 20, "bold"),bd=3,
                   highlightbackground=backgroundColor_GUI[0],
                   bg=backgroundColor_GUI[2], command=lambda: showBtnClick("-"))
minus_btn.place(x=241, y=179)

Plus_btn = Button(btn_frame, text="+", padx=20, pady=2, fg="black",font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[2], command=lambda: showBtnClick("+"))
Plus_btn.place(x=240, y=240)

number_0 = Button(btn_frame, text="0", padx=19, pady=2, fg="black",font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[0], command=lambda: showBtnClick(0))
number_0.place(x=80, y=240)

clear_btn = Button(btn_frame, text="C", padx=18, pady=2, fg="black", font=("arial", 20, "bold"),bd=3,
                   highlightbackground=backgroundColor_GUI[0],
                   bg=backgroundColor_GUI[2], command=lambda: btnClear())
clear_btn.place(x=0, y=240)

equals_btn = Button(btn_frame, text="=", padx=19, pady=2, fg="black", font=("arial", 20, "bold"),bd=3,
                    highlightbackground=backgroundColor_GUI[0],
                    bg=backgroundColor_GUI[2], command=lambda: equalsBtn())
equals_btn.place(x=160, y=240)

number_1 = Button(btn_frame, text="1", padx=20, pady=2, fg="black", font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[0], command=lambda: showBtnClick(1))
number_1.place(x=0, y=179)

number_2 = Button(btn_frame, text="2", padx=20, pady=2, fg="black",font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[0], command=lambda: showBtnClick(2))
number_2.place(x=80, y=179)

number_3 = Button(btn_frame, text="3",padx=20, pady=2, fg="black",font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[0], command=lambda: showBtnClick(3))
number_3.place(x=160, y=179)

number_4 = Button(btn_frame, text="4", padx=20, pady=2, fg="black",font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[0], command=lambda: showBtnClick(4))
number_4.place(x=0, y=118)

number_5 = Button(btn_frame, text="5", padx=20, pady=2, fg="black", font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[0], command=lambda: showBtnClick(5))
number_5.place(x=80, y=118)

number_6 = Button(btn_frame, text="6", padx=20, pady=2, fg="black", font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[0], command=lambda: showBtnClick(6))
number_6.place(x=160, y=118)

number_7 = Button(btn_frame, text="7", padx=20, pady=2, fg="black", font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[0], command=lambda: showBtnClick(7))
number_7.place(x=0, y=58)

number_8 = Button(btn_frame, text="8", padx=20, pady=2, fg="black", font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[0], command=lambda: showBtnClick(8))
number_8.place(x=80, y=58)

number_9 = Button(btn_frame, text="9", padx=20, pady=2, fg="black", font=("arial", 20, "bold"),bd=3,
                  highlightbackground=backgroundColor_GUI[0],
                  bg=backgroundColor_GUI[0], command=lambda: showBtnClick(9))
number_9.place(x=160, y=58)

# ================================= Labels and Entries =====================================

label = Label(my_calc, text="Standard Calculation", font=("Times New Roman", 15, "bold"), bg=backgroundColor_GUI[0])
label.place(x=0, y=5)

res_entry = Entry(my_calc, textvariable=value_res, bg=backgroundColor_GUI[2], font=("arial", 20, "bold"), bd=30,
                  insertwid=4, justify="right")
res_entry.pack(side=LEFT)

my_calc.mainloop()
