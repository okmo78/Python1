import tkinter as tk

window = tk.Tk()
window.geometry("500x500+100+100")

def evenOdd(x):
    if (x % 2 == 0):
        return 2
    else:
        return 1
    
result1 = evenOdd(2)
result2 = evenOdd(3)

input1 = tk.Entry(textvariable="mo")
input1.pack()

print(result1)

tk.mainloop()