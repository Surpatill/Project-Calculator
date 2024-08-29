import tkinter as tk
import math
calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(0,"end")
    text_result.insert(0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(0,"end")
        text_result.insert(0,calculation)
    except:
        clear_field()
        text_result.insert(0,"Error")
        
def square():
    global calculation
    try:
        calculation = str(eval(calculation) ** 2)
        text_result.delete(0,"end")
        text_result.insert(0,calculation)
    except:
        clear_field()
        text_result.insert(0,"Error")
        
def sqrt():
    global calculation
    try:
        calculation = str(eval(calculation) ** 0.5)
        text_result.delete(0,"end")
        text_result.insert(0,calculation)
    except:
        clear_field()
        text_result.insert(0,"Error")
        
def factorial():
    global calculation
    try:
        calculation = str(math.factorial(int(calculation)))
        text_result.delete(0,"end")
        text_result.insert(0,calculation)
    except:
        clear_field()
        text_result.insert(0,"Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(0,"end")
    
def backspace():
    global calculation
    calculation=calculation[:-1]
    text_result.delete(0,"end")
    text_result.insert(0,calculation)

root=tk.Tk()
root.title("Simple Calculator")
root.geometry("430x330")
root.resizable(False,False)

root.configure(bg="#17161b")

text_result=text_result = tk.Entry(root, font=("Arial", 24), width=25, borderwidth=5, relief="ridge")
text_result.grid(row=0, column=0, columnspan=6)

for i in range(6):
    root.grid_columnconfigure(i, weight=1)

btn_1=tk.Button(root,text="1", command=lambda: add_to_calculation(1),width=6,bd=2,bg="pink",fg="red",relief="groove",font=("Arial",14))
btn_1.grid(row=2, column=1,padx=5,pady=5)
btn_2=tk.Button(root,text="2", command=lambda: add_to_calculation(2),width=6,bd=2,bg="pink",fg="red",relief="groove",font=("Arial",14))
btn_2.grid(row=2, column=2,padx=5,pady=5)
btn_3=tk.Button(root,text="3", command=lambda: add_to_calculation(3),width=6,bd=2,bg="pink",fg="red",relief="groove",font=("Arial",14))
btn_3.grid(row=2, column=3,padx=5,pady=5)
btn_4=tk.Button(root,text="4", command=lambda: add_to_calculation(4),width=6,bd=2,bg="pink",fg="red",relief="groove",font=("Arial",14))
btn_4.grid(row=3, column=1,padx=5,pady=5)
btn_5=tk.Button(root,text="5", command=lambda: add_to_calculation(5),width=6,bd=2,bg="pink",fg="red",relief="groove",font=("Arial",14))
btn_5.grid(row=3, column=2,padx=5,pady=5)
btn_6=tk.Button(root,text="6", command=lambda: add_to_calculation(6),width=6,bd=2,bg="pink",fg="red",relief="groove",font=("Arial",14))
btn_6.grid(row=3, column=3,padx=5,pady=5)
btn_7=tk.Button(root,text="7", command=lambda: add_to_calculation(7),width=6,bd=2,bg="pink",fg="red",relief="groove",font=("Arial",14))
btn_7.grid(row=4, column=1,padx=5,pady=5)
btn_8=tk.Button(root,text="8", command=lambda: add_to_calculation(8),width=6,bd=2,bg="pink",fg="red",relief="groove",font=("Arial",14))
btn_8.grid(row=4, column=2,padx=5,pady=5)
btn_9=tk.Button(root,text="9", command=lambda: add_to_calculation(9),width=6,bd=2,bg="pink",fg="red",relief="groove",font=("Arial",14))
btn_9.grid(row=4, column=3,padx=5,pady=5)
btn_0=tk.Button(root,text="0", command=lambda: add_to_calculation(0),width=6,bd=2,bg="pink",fg="red",relief="groove",font=("Arial",14))
btn_0.grid(row=5, column=2,padx=5,pady=5)
btn_plus=tk.Button(root,text="+", command=lambda: add_to_calculation("+"),width=6,bd=2,bg="sky blue",fg="navy",relief="groove",font=("Arial",14))
btn_plus.grid(row=2, column=4,padx=5,pady=5)
btn_min=tk.Button(root,text="-", command=lambda: add_to_calculation("-"),width=6,bd=2,bg="sky blue",fg="navy",relief="groove",font=("Arial",14))
btn_min.grid(row=3, column=4,padx=5,pady=5)
btn_mul=tk.Button(root,text="*", command=lambda: add_to_calculation("*"),width=6,bd=2,bg="sky blue",fg="navy",relief="groove",font=("Arial",14))
btn_mul.grid(row=4, column=4,padx=5,pady=5)
btn_div=tk.Button(root,text="/", command=lambda: add_to_calculation("/"),width=6,bd=2,bg="sky blue",fg="navy",relief="groove",font=("Arial",14))
btn_div.grid(row=5, column=4,padx=5,pady=5)
btn_open=tk.Button(root,text="(", command=lambda: add_to_calculation("("),width=6,bd=2,bg="sky blue",fg="navy",relief="groove",font=("Arial",14))
btn_open.grid(row=5, column=1,padx=5,pady=5)
btn_close=tk.Button(root,text=")", command=lambda: add_to_calculation(")"),width=6,bd=2,bg="sky blue",fg="navy",relief="groove",font=("Arial",14))
btn_close.grid(row=5, column=3,padx=5,pady=5)
btn_sqr=tk.Button(root,text="x²", command=square,width=6,bd=2,bg="sky blue",fg="navy",relief="groove",font=("Arial",14))
btn_sqr.grid(row=6, column=4,padx=5,pady=5)
btn_sqrt=tk.Button(root,text="√x", command=sqrt,width=6,bd=2,bg="sky blue",fg="navy",relief="groove",font=("Arial",14))
btn_sqrt.grid(row=6, column=3,padx=5,pady=5)
btn_fact=tk.Button(root,text="x!", command=factorial,width=6,bd=2,bg="sky blue",fg="navy",relief="groove",font=("Arial",14))
btn_fact.grid(row=6, column=2,padx=5,pady=5)
btn_decimal=tk.Button(root,text=".", command=lambda: add_to_calculation("."),width=6,bd=2,bg="sky blue",fg="navy",relief="groove",font=("Arial",14))
btn_decimal.grid(row=6, column=1,padx=5,pady=5)

btn_equals=tk.Button(root,text="=", command=evaluate_calculation,width=6,bd=2,bg="sienna3",fg="black",relief="groove",font=("Arial",14))
btn_equals.grid(row=7, column=4,padx=5,pady=5)
btn_clear=tk.Button(root,text="AC", command=clear_field,width=6,bd=2,bg="sienna3",fg="black",relief="groove",font=("Arial",14))
btn_clear.grid(row=7, column=3,padx=5,pady=5)
btn_backspace=tk.Button(root,text="C", command=backspace,width=6,bd=2,bg="sienna3",fg="black",relief="groove",font=("Arial",14))
btn_backspace.grid(row=7, column=2,padx=5,pady=5)

root.mainloop()


