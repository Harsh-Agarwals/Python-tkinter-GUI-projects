# importing needed tkinter function
import tkinter as tk

# defining window, title, and size of window
window = tk.Tk()
window.title("CALCULATOR")
window.resizable(0, 0)

# Taking input as string
v = tk.StringVar()

# Defining Entry widget to take the input
inp = tk.Entry(master=window, borderwidth=5, width=30, textvariable=v)
inp.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Defining frame for buttons which will consist of all buttons
btns = tk.Frame(master=window).grid()

# Function to be executed on clicking num button
def btn_click(num):
    inp.insert(tk.END, num)

# Function to be executed on clicking clear button
def btn_clear():
    inp.delete(0, tk.END)

# Function to be executed on clicking sign button(+,-,*,/)
def btn_cmd(sign):
    entry = inp.get()
    inp.delete(0, tk.END)
    inp.insert(0, entry + " " + str(sign) + " ")

# Function giving result
def equal():
    entry = inp.get()
    inp.delete(0, tk.END)
    inp.insert(0, eval(entry))

# Defining and designing all numbers, signs, decimal, equal, clear and exit buttons

btn7 = tk.Button(btns, text="7", padx=10, width=5, command= lambda: btn_click(7)).grid(row=1, column=0, padx=2, pady=1)
btn8 = tk.Button(btns, text="8", padx=10, width=5, command= lambda: btn_click(8)).grid(row=1, column=1, padx=2, pady=1)
btn9 = tk.Button(btns, text="9", padx=10, width=5, command= lambda: btn_click(9)).grid(row=1, column=2, padx=2, pady=1)

btn4 = tk.Button(btns, text="4", padx=10, width=5, command= lambda: btn_click(4)).grid(row=2, column=0, padx=2, pady=1)
btn5 = tk.Button(btns, text="5", padx=10, width=5, command= lambda: btn_click(5)).grid(row=2, column=1, padx=2, pady=1)
btn6 = tk.Button(btns, text="6", padx=10, width=5, command= lambda: btn_click(6)).grid(row=2, column=2, padx=2, pady=1)

btn1 = tk.Button(btns, text="1", padx=10, width=5, command= lambda: btn_click(1)).grid(row=3, column=0, padx=2, pady=1)
btn2 = tk.Button(btns, text="2", padx=10, width=5, command= lambda: btn_click(2)).grid(row=3, column=1, padx=2, pady=1)
btn3 = tk.Button(btns, text="3", padx=10, width=5, command= lambda: btn_click(3)).grid(row=3, column=2, padx=2, pady=1)

zero = tk.Button(btns, text="0", padx=10, width=5, command= lambda: btn_click(0)).grid(row=4, column=0, padx=2, pady=1)
dot = tk.Button(btns, text=".", padx=10, width=5, command= lambda: btn_click(".")).grid(row=4, column=1, padx=2, pady=1)
clear = tk.Button(btns, text="Clear", padx=10, width=5, command= btn_clear).grid(row=4, column=2, padx=2, pady=1)

add = tk.Button(btns, text="+", padx=10, width=5, command= lambda: btn_cmd("+")).grid(row=5, column=0, padx=2, pady=1)
sub = tk.Button(btns, text="-", padx=10, width=5, command= lambda: btn_cmd("-")).grid(row=5, column=1, padx=2, pady=1)
mul = tk.Button(btns, text="*", padx=10, width=5, command= lambda: btn_cmd("*")).grid(row=5, column=2, padx=2, pady=1)

div = tk.Button(btns, text="/", padx=10, width=5, command= lambda: btn_cmd("/")).grid(row=6, column=0, padx=2, pady=1)
eql = tk.Button(btns, text="=", padx=10, width=15, command= equal, bd=3, bg="#fff").grid(row=6, column=1, columnspan=2, padx=2, pady=1)

ext = tk.Button(btns, text="QUIT", padx=10, pady=5, width=25, command=window.quit, bg="green", fg="yellow", bd=3).grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# executing mainloop() that traces the activities inside window and run the program
window.mainloop()