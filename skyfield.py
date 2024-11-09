import tkinter as tk
import tkinter.messagebox as msg

window_1 = tk.Tk()

class window():
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width


def hello():
    print("hello World!")

hello()

new_window = window(height=50,width=50)

print(new_window.height)

text1 = tk.Label(text=new_window.width)
text1.pack()

tk.mainloop()

