import tkinter as tk
import tkinter.messagebox as msg

window_1 = tk.Tk()
window_1.geometry("500x700")

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

text4 = tk.Button(window_1, text="Hello", font="./font/sylfaen.ttf", bg="cyan")
text4.pack()

text5 = tk.Scrollbar(window_1)
text5.pack()

text6 = tk.Listbox(window_1, bg="cyan")
text6.pack()

text7 = tk.Checkbutton(window_1)
text7.pack()

text8 = tk.Checkbutton(window_1, text="A", font="Bold")
text8.pack()

tk.mainloop()
