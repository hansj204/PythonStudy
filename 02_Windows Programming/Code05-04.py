from tkinter import *
window = Tk()

window.title('고양이들')

photo1 = PhotoImage(file = "image/GIF/cat.gif")
label1 = Label(window, image = photo1)

photo2 = PhotoImage(file = "image/GIF/cat2.gif")
label2 = Label(window, image = photo2)

label1.pack(side=LEFT)
label2.pack()

window.mainloop()
