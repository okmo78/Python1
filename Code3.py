from tkinter import *

window = Tk()
window.geometry("500x500")

def man(firstname, lastname):
    return firstname + lastname

picture = PhotoImage(file="flower.png")
text = Label(image= picture, text=man("Mohammad", "Okhrati"))
text.pack()

mainloop()