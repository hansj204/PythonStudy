from tkinter import *
from tkinter import messagebox

def myFunc() :
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽져?")

window = Tk()

photo = PhotoImage(file = "image/GIF/dog2.gif")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

window.mainloop()