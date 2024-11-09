import tkinter as tk
import tkinter.messagebox as msg

window_1 = tk.Tk()
window_1.geometry("500x500")

class window():
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

img = tk.PhotoImage(file="./image/flower.png")
text1 = tk.Label(window_1, text="100")
text1.pack()

text2 = tk.Label(window_1, bg="blue", image=img)
text2.pack()

text3 = tk.Label(window_1, text="hello", font="./font/sylfaen.ttf")
text3.pack()

tk.mainloop()

