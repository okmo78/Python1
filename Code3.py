from tkinter import *

window = Tk()
window.geometry("500x500")

def man(firstname, lastname):
    return firstname + lastname

text = Label(text=man("Mohammad", "Okhrati"))
text.pack()

picture = Label(image="flower1.png")
picture.pack()

mainloop()