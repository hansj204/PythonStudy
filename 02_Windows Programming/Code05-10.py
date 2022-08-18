from textwrap import fill
from tkinter import *
window = Tk()

btnList = [None] * 3

for i in range(0, 3) :
    btnList[i] = Button(window, text = "버튼" + str(i + 1))

for btn in btnList :
    #btn.pack(side = RIGHT)
     btn.pack(side = TOP, fill = X, padx = 10, pady = 10)

window.mainloop()
