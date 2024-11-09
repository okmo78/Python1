from tkinter import *

window = Tk()
window.minsize(200,200)

def add(num1: int, num2: int) -> int:
    """add two numbers"""
    num3 = num1 + num2

    return num3

num1, num2 = 5, 15
ans = add(num1 , num2)
print(f"The addition of {num1} and {num2} resuts {ans}")

text = Label(text=ans, font="TkDefaultFont")
text.pack()

mainloop()
