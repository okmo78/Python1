from tkinter import *

window_1 = Tk()

class window():
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

def hello():
    print("hello World!")

hello()

new_window = window(height=50,width=50)

print(new_window.height)

text = Label(window_1, text=window_1)
text1 = Label(text=new_window.width)
text.pack()
text1.pack()

mainloop()